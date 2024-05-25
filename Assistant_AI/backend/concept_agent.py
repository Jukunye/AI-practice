from crewai import Agent, Task, Crew


async def concepts(prompt):

    researcher = Agent(
        role='Researcher',
        goal='Find relevant information.',
        backstory='A great teacher with years of experience.',
        allow_delegation=False,
        # verbose=True
    )

    research_concepts_task = Task(
        description=f"Can you create a mental map or diagram of the concepts mentioned in the prompt? \
        Are there any relationships or connections between these concepts? \
        Can you summarize the main concepts mentioned in the prompt? \
        Are there any key takeaways or insights that can be extracted from the prompt? \
        This is the prompt <<{prompt}>>",
        expected_output='A overview of the concepts from the prompt',
        # async_execution=True,
        agent=researcher,
    )

    crew = Crew(
        agents=[researcher],
        tasks=[research_concepts_task],
        verbose=2
    )

    return (crew.kickoff())
