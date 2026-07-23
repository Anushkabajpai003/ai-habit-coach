"""
Verifies connection to the Anthropic Claude API.
NOTE: As of Day 3, this will show a "credit balance too low" error,
which is expected — the account has no API credits yet. The app itself
uses ai_coach.py's mock mode instead, so this is not a blocker.
This script exists so we can quickly re-test once credits are added.
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Say hello in one short encouraging sentence about building a new habit."}
    ]
)

print(response.content[0].text)