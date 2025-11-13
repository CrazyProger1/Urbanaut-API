from decouple import config

GOOGLE_GEMINI_API_KEY = config("GOOGLE_GEMINI_API_KEY")

# Abandoned app AI settings
ABANDONED_AI_SEARCH_ENGINE_INSTRUCTIONS = """
You are a filter extraction assistant for urbex website.
Return only valid JSON with keys:
"tags" — array of strings
Allowed tags: {tags}
No markdown or extra text.
Example:
Input: some underground staff
Output: {"tags":["underground","industrial","cave","metro","bunker","mine"]}
"""

ABANDONED_AI_SEARCH_ENGINE = "src.apps.abandoned.services.ai.gemini.GoogleGeminiAbandonedAISearchEngine"
