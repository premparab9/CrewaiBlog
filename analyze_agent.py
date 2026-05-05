from crewai import Agent

def create_analyze_agent():
    agent = Agent(
        role="Content Analyzer",
        goal="Analyze transcript and extract key insights",
        backstory="Expert in breaking down educational content",
        verbose=True,
        allow_delegation=False,
    )
    return agent

