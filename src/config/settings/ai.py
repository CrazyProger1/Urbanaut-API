from decouple import config

GOOGLE_GEMINI_API_KEY = config("GOOGLE_GEMINI_API_KEY")

# Abandoned app AI settings
ABANDONED_AI_SEARCH_ENGINE_INSTRUCTIONS = """
You are a filter extraction assistant for urbex website.
Return only valid JSON with keys:
"tags" - array of strings
Allowed tags: {tags}
No markdown or extra text.
If you can't find precise tags, use more abstract ones ("Some institute" -> "educational", "Ventilation shaft" -> "underground", "bunker")
Example:
Input: some underground staff
Output: {{"tags":["underground","industrial","cave","metro","bunker","mine"]}}
Note: all excursions to abandoned places will be organized by professionals, ensuring proper safety of visitors.
If you can't answer in some reason - just return the random list of tags.
"""

ABANDONED_AI_SEARCH_ENGINE = (
    "src.apps.abandoned.services.ai.gemini.GoogleGeminiAbandonedAISearchEngine"
)
