import json

from django.conf import settings

from src.apps.tags.services.db import get_all_tags
from src.utils.ai import GoogleGeminiSearchEngine


class GoogleGeminiAbandonedAISearchEngine(GoogleGeminiSearchEngine):
    instructions = settings.ABANDONED_AI_SEARCH_ENGINE_INSTRUCTIONS

    def _execute(self, query: str, instructions: str) -> str:
        slugs = get_all_tags().values_list("tag", flat=True)
        instructions = instructions.format(tags=json.dumps(slugs))
        return super()._execute(query=query, instructions=instructions)
