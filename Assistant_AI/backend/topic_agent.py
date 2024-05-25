from crewai import Agent, Task, Crew


async def topics(prompt):
    researcher = Agent(
        role='Researcher',
        goal='Find relevant information.',
        backstory='A great teacher with years of experience.',
        allow_delegation=False,
        # verbose=True
    )

    research_topics_task = Task(
        description=f"What are the underlying topics or themes mentioned in the prompt? \
        Are there any dominant or emerging topics? \
        What are the most important keywords or phrases mentioned in the prompt? \
        Are there any specific terms or jargon related to the topic? \
        This is the prompt <<{prompt}>>",
        expected_output='A overview of the topics and keywords from the prompt',
        # async_execution=True,
        agent=researcher,
    )

    crew = Crew(
        agents=[researcher],
        tasks=[research_topics_task],
        verbose=2
    )

    return (crew.kickoff())
