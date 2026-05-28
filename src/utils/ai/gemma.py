import json
import logging

from ollama import chat

from src.utils.ai.types import BaseAIAssistant, BaseAISearchSearchEngine
from src.utils.cache import func_cache
from src.utils.django.settings import default_settings

default_settings.setdefault("GOOGLE_GEMMA_ENABLE_CACHE", True)
default_settings.setdefault("GOOGLE_GEMMA_CACHE_EXPIRATION", None)
default_settings.setdefault("GOOGLE_GEMMA_CACHE_PREFIX", "gemma_cache")
default_settings.setdefault("GOOGLE_GEMMA_MODEL", "gemma3:1b")
default_settings.setdefault("GOOGLE_GEMMA_NUM_CTX", 1024 * 4)
default_settings.setdefault("GOOGLE_GEMMA_NUM_PREDICT", 256)
default_settings.setdefault("GOOGLE_GEMMA_TEMPERATURE", 0)
default_settings.setdefault(
    "GOOGLE_GEMMA_SEARCH_ENGINE_INSTRUCTIONS",
    "Return only valid JSON. No markdown or extra text.",
)

logger = logging.getLogger(__name__)


class GoogleGemmaAIAssistant(BaseAIAssistant):
    def __init__(
        self,
        model: str = default_settings.GOOGLE_GEMMA_MODEL,
        cache_enabled: bool = default_settings.GOOGLE_GEMMA_ENABLE_CACHE,
        cache_expiration: int = default_settings.GOOGLE_GEMMA_CACHE_EXPIRATION,
        cache_prefix: str = default_settings.GOOGLE_GEMMA_CACHE_PREFIX,
        num_ctx: int = default_settings.GOOGLE_GEMMA_NUM_CTX,
        num_predict: int = default_settings.GOOGLE_GEMMA_NUM_PREDICT,
        temperature: int = default_settings.GOOGLE_GEMMA_TEMPERATURE,
    ):
        self._model = model
        self._cache_enabled = cache_enabled
        self._cache_exp = cache_expiration
        self._cache_prefix = cache_prefix
        self._num_ctx = num_ctx
        self._num_predict = num_predict
        self._temperature = temperature

    def _execute(self, query: str, instructions: str | None = None) -> str:
        logger.info('Executing query "%s"', query)

        if not instructions:
            instructions = query
        else:
            query = f"{instructions}\n\nQuery: {query}"

        response = chat(
            model=self._model,
            messages=[{"role": "user", "content": query}],
            options={"num_ctx": self._num_ctx, "num_predict": self._num_predict, "temperature": self._temperature},
        )
        text = response.message.content
        logger.info("Query result: %s", text)

        if not text:
            logger.warning("Got empty response")
            return ""

        return text

    def execute(self, query: str, instructions: str | None = None) -> str:
        if self._cache_enabled:
            return func_cache(prefix=self._cache_prefix, exp=self._cache_exp)(
                target=self._execute,
            )(
                query=query,
                instructions=instructions,
            )
        return self._execute(query=query, instructions=instructions)


class GoogleGemmaSearchEngine(GoogleGemmaAIAssistant, BaseAISearchSearchEngine):
    instructions: str = default_settings.GOOGLE_GEMMA_SEARCH_ENGINE_INSTRUCTIONS

    def __init__(self, instructions: str | None = None, **kwargs):
        self._search_instructions = instructions or self.instructions
        super().__init__(**kwargs)

    def search(self, query: str) -> dict:
        response = self.execute(
            query=query,
            instructions=self._search_instructions,
        )
        response = response.removeprefix("```json").removesuffix("```").strip()
        try:
            return json.loads(response)
        except json.decoder.JSONDecodeError:
            return {}
