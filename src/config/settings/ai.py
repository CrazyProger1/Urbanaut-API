from decouple import config

GOOGLE_GEMINI_API_KEY = config("GOOGLE_GEMINI_API_KEY")

# Abandoned app AI settings
ABANDONED_AI_SEARCH_ENGINE_INSTRUCTIONS = """
You are a tag extractor for an urbex (urban exploration) search engine.
Given a user query, return ONLY a JSON object with key "tags" — an array of matching tags chosen STRICTLY from this list: {tags}
Rules:
- Use ONLY tags from the list above. Never invent new tags.
- Pick 1-5 most relevant tags. If nothing matches, return {{"tags":[]}}.
- No markdown, no explanation, no extra text — JSON only.
Example output: {{"tags":["underground","industrial"]}}
"""

ABANDONED_AI_SEARCH_ENGINE = (
    "src.apps.abandoned.services.ai.gemma.GoogleGemmaAbandonedAISearchEngine"
)
