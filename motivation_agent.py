from crewai import Agent, Task, Crew
from dotenv import load_dotenv
load_dotenv()


question = input('How can I help you? ')

motivetor = Agent(
    role='Motivation speaker',
    goal='Give inspirational and informative speech',
    backstory='You are an expert teacher for python.',
    verbose=True
)

task = Task(
    description=f'Motivate in relation to this statement {question}',
    expected_output='A bullet list summary of the motivation',
    agent=motivetor
)

crew = Crew(
    agents=[motivetor],
    tasks=[task],
    verbose=2
)

result = crew.kickoff()

print(result)
