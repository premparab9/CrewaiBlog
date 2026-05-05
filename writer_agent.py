from crewai import Agent

def create_writer_agent():
    agent = Agent(
        role="Blog Writer",
        goal="Write an engaging Medium-style blog",
        backstory="Professional content writer",
        verbose=True,
        allow_delegation=False,
    )
    return agent