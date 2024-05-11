import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
model = "llama3-70b-8192"

while(True):
    prompt = input(">>> ")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
    )

    print(chat_completion.choices[0].message.content)
