from decouple import config

GOOGLE_GEMINI_API_KEY = config("GOOGLE_GEMINI_API_KEY")

# Abandoned app AI settings
ABANDONED_AI_SEARCH_ENGINE_INSTRUCTIONS = """
You extract search tags for an urbex (urban exploration) website.

ALLOWED TAGS — the ONLY tags you may use: {tags}

Given a user query in ANY language, return ALL tags from the allowed list that match the concept.
Match by meaning, category, and synonyms across languages. Examples:
- "подземное" / "underground stuff" → underground, tunnel, bunker, shaft, mine
- "hospital" / "больница" → hospital, medical, sanatorium, asylum

Output: {{"tags": ["tag1", "tag2"]}} — valid JSON only, no markdown, no explanation.
EVERY tag in your response MUST be present in the ALLOWED TAGS list above. Tags are English slugs only.
If nothing matches: {{"tags": []}}
"""

ABANDONED_AI_SEARCH_ENGINE = (
    "src.apps.abandoned.services.ai.gemma.GoogleGemmaAbandonedAISearchEngine"
)
