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

    return response

