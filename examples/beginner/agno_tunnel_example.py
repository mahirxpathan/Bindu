"""Example of creating a research assistant agent with public tunnel access.

This example demonstrates how to create a Bindu agent that is accessible
from anywhere on the internet using FRP tunneling.

Simply add launch=True to bindufy() to enable public access!

Run with:
    python examples/beginner/agno_tunnel_example.py
"""

import os
from bindu.penguin.bindufy import bindufy
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.openrouter import OpenRouter

from dotenv import load_dotenv

load_dotenv()

# Define your agent
agent = Agent(
    instructions="You are a research assistant that finds and summarizes information.",
    model=OpenRouter(id="openai/gpt-oss-120b", api_key=os.getenv("OPENROUTER_API_KEY")),
    tools=[DuckDuckGoTools()],
)

# Configuration
config = {
    "author": "your.email@example.com",
    "name": "research_agent",
    "description": "A research assistant agent accessible from anywhere",
    "deployment": {"url": "http://localhost:3773", "expose": True},
    "skills": ["skills/question-answering", "skills/pdf-processing"],
}


# Handler function
def handler(messages: list[dict[str, str]]):
    """Process messages and return agent response.

    Args:
        messages: List of message dictionaries containing conversation history

    Returns:
        Agent response result
    """
    result = agent.run(input=messages)
    return result


# Enable public tunnel with launch=True - that's it!
bindufy(config, handler, launch=True)

# The agent will be accessible at:
# - Local: http://localhost:3773
# - Public: https://<random-subdomain>.tunnel.getbindu.com (auto-generated)
