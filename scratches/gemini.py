from decouple import config
from dotenv import load_dotenv
from google import genai
from google.genai import types

SYSTEM_INSTRUCTIONS = """
You are a filter extraction assistant for urbex website.
Return only valid JSON with keys:
"tags" — array of strings
Allowed tags: [
  "urban",
  "ruins",
  "industrial",
  "underground",
  "nature",
  "tunnels",
  "historic",
  "metro",
  "cave",
  "bunker",
  "abandoned",
  "factory",
  "mine",
  "sewer",
  "bridge",
  "roof",
  "fortress",
  "railway",
  "subway",
  "basement",
  "warehouse",
  "military",
  "restricted",
  "hidden",
  "forgotten",
  "exploration",
  "digging",
  "catacombs",
  "construction",
  "archive"
]
No markdown or extra text.
Example:
Input: some underground staff
Output: {"tags":["underground","industrial","cave","metro","bunker"]}
"""


def main():
    load_dotenv()
    client = genai.Client(api_key=config("GOOGLE_GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents="Подземка с рельсами и вагонетками",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0),
            system_instruction=SYSTEM_INSTRUCTIONS,
        ),
    )
    print(response.text)


if __name__ == "__main__":
    main()
