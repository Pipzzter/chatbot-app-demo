import markdown
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def chatbot(prompt):

    # Make a streaming request to the OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        stream=True  # Enable streaming
    )
    #
    # for chunk in response:
    #     print(
    #         chunk.choices[0].delta.content,
    #         end="",
    #         flush=True
    #     )
    #     content = chunk.choices[0].delta.content if chunk.choices[0].delta.content else ""
    #     yield content
    return response

