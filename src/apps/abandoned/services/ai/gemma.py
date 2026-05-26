from django.conf import settings

from src.apps.tags.services.db import get_all_tags
from src.utils.ai import GoogleGemmaSearchEngine


class GoogleGemmaAbandonedAISearchEngine(GoogleGemmaSearchEngine):
    instructions = settings.ABANDONED_AI_SEARCH_ENGINE_INSTRUCTIONS

    def _get_valid_slugs(self) -> set[str]:
        return set(get_all_tags().values_list("tag", flat=True).distinct())

    def _execute(self, query: str, instructions: str | None = None) -> str:
        if instructions:
            slugs = self._get_valid_slugs()
            instructions = instructions.format(tags=", ".join(sorted(slugs)))
        return super()._execute(query=query, instructions=instructions)

    def search(self, query: str) -> dict:
        result = super().search(query=query)
        if tags := result.get("tags"):
            valid = self._get_valid_slugs()
            result["tags"] = [tag for tag in tags if tag in valid]
        return result
