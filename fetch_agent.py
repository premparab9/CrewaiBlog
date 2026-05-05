from crewai import Agent
from tools.youtube_tool import get_transcript



def create_fetch_agent():
    agent = Agent(
        role="YouTube Transcript Fetcher",
        goal="Extract transcript from YouTube video",
        backstory="Expert in extracting clean transcripts",
        verbose=True,
        allow_delegation=False,
        tools=[get_transcript],
    )
    return agent

