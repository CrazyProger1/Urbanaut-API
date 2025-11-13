import json
import logging

from google import genai
from google.genai import types

from src.utils.ai.types import BaseAIAssistant, BaseAISearchSearchEngine
from src.utils.cache import redcache
from src.utils.django.settings import default_settings

default_settings.setdefault("GOOGLE_GEMINI_ENABLE_CACHE", True)
default_settings.setdefault("GOOGLE_GEMINI_CACHE_EXPIRATION", 10000)
default_settings.setdefault("GOOGLE_GEMINI_CACHE_PREFIX", "gemini_cache")
default_settings.setdefault("GOOGLE_GEMINI_MODEL", "gemini-2.5-flash-lite")
default_settings.setdefault(
    "GOOGLE_GEMINI_SEARCH_ENGINE_INSTRUCTIONS",
    "Return only valid JSON. No markdown or extra text.",
)

logger = logging.getLogger(__name__)


class GoogleGeminiAIAssistant(BaseAIAssistant):
    def __init__(
            self,
            api_key: str = default_settings.GOOGLE_GEMINI_API_KEY,
            model: str = default_settings.GOOGLE_GEMINI_MODEL,
            cache_enabled: bool = default_settings.GOOGLE_GEMINI_ENABLE_CACHE,
            cache_expiration: int = default_settings.GOOGLE_GEMINI_CACHE_EXPIRATION,
            cache_prefix: str = default_settings.GOOGLE_GEMINI_CACHE_PREFIX,
    ):
        self._api_key = api_key
        self._client = genai.Client(api_key=api_key)
        self._model = model
        self._cache_enabled = cache_enabled
        self._cache_exp = cache_expiration
        self._cache_prefix = cache_prefix

    def _execute(self, query: str, instructions: str) -> str:
        logger.debug("Executing query %s with instructions %s", query, instructions)
        response = self._client.models.generate_content(
            model=self._model,
            contents=query,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0),
                system_instruction=instructions,
            ),
        )
        logger.debug("Query result: %s", response)
        return response.text

    def execute(self, query: str, instructions: str = None) -> str:
        if self._cache_enabled:
            return redcache(
                prefix=self._cache_prefix,
                exp=self._cache_exp
            )(
                target=self._execute,
            )(
                query=query,
                instructions=instructions,
            )
        return self._execute(query=query, instructions=instructions)


class GoogleGeminiSearchEngine(GoogleGeminiAIAssistant, BaseAISearchSearchEngine):
    instructions: str = default_settings.GOOGLE_GEMINI_SEARCH_ENGINE_INSTRUCTIONS

    def __init__(self, instructions: str = None, **kwargs):
        self._search_instructions = instructions or self.instructions
        super().__init__(**kwargs)

    def search(self, query: str) -> dict:
        response = self.execute(
            query=query,
            instructions=self._search_instructions,
        )
        return json.loads(response)
