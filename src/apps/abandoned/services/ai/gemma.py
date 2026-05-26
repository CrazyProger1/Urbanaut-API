from django.conf import settings

from src.apps.tags.services.db import get_all_tags
from src.utils.ai import GoogleGemmaSearchEngine


class GoogleGemmaAbandonedAISearchEngine(GoogleGemmaSearchEngine):
    instructions = settings.ABANDONED_AI_SEARCH_ENGINE_INSTRUCTIONS

    def _execute(self, query: str, instructions: str | None = None) -> str:
        if instructions:
            slugs = list(get_all_tags().values_list("tag", flat=True).distinct())
            instructions = instructions.format(tags=", ".join(sorted(slugs)))
        return super()._execute(query=query, instructions=instructions)
