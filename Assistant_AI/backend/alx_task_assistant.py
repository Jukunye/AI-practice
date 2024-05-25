from groq import Groq
import os
import asyncio
from crewai import Agent, Task, Crew
from concept_agent import concepts
from topic_agent import topics
from steps_agent import breakdown
from dotenv import load_dotenv
load_dotenv()


# client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
# model = "llama3-70b-8192"


async def ai_assistant(prompt):

    # prompt = input('Question:- ')

    concept = await concepts(prompt)
    topic = await topics(prompt)
    step = await breakdown(prompt)

    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": f"Simplify this blog: {concept + topic + step}",
    #         }
    #     ],
    #     model=model,
    # )

    # print(concept)
    # print(topic)
    # print(step)
    # print(chat_completion.choices[0].message.content)

    return concept + "\n\n" + topic + "\n\n" + step
