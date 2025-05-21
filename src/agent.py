# from google adk import search

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

dice_agent = LlmAgent(
      model="gemini-2.0-flash-exp",
      name="janos_agent",
      description="Este agente sirve para darte la hora",
      instruction="""res`pmd tp tje query using google search""",
      tools=[google_search],
)

import datetime
from zoneinfo import ZoneInfo
from google.adk import Agent

def get_waether(city: str) -> dict:

