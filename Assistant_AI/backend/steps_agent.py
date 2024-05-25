from crewai import Agent, Task, Crew


async def breakdown(prompt):
    developer = Agent(
        role='Teacher',
        goal='Break down project into tasks',
        backstory='An experienced developer and a great teacher with years of experience.',
        allow_delegation=False,
        # verbose=True
    )

    steps_task = Task(
        description=f"How can I break down this complex project into smaller, \
        manageable tasks?. The following is the project: <<{prompt}>>",
        expected_output="A overview of the tasks from the prompt",
        # async_execution=True,
        agent=developer,
    )

    crew = Crew(
        agents=[developer],
        tasks=[steps_task],
        verbose=2
    )

    return (crew.kickoff())
