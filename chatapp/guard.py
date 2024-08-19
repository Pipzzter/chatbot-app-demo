from fuzzywuzzy import fuzz


def guard_check(content, client):
    chat_completion = client.chat.completions.create(
        model="tgi",
        messages=[
            {
                "role": "user",
                "content": content
            }
        ],
        stream=True,
        max_tokens=20
    )
    flag = True
    for message in chat_completion:
        if message.choices[0].delta.content == "unsafe":
            flag = False

    return flag


ALLOWED_TOPICS = [
    "diamond types", "diamond cuts", "diamond shapes", "diamond clarity",
    "diamond color", "diamond carat weight", "diamond certification",
    "diamond settings", "diamond pricing", "ring styles", "ring metals",
    "ring sizes", "engagement rings", "wedding bands", "custom rings",
    "jewelry care", "jewelry trends", "gift ideas", "return policies",
    "warranty information", "order status", "buying guides", "glossary", "faqs", "rings"
]


def is_question_within_topic_fuzzy(question: str, allowed_topics: list = ALLOWED_TOPICS):
    for topic in allowed_topics:
        if fuzz.partial_ratio(topic.lower(), question.lower()) > 70:
            return True

    return False
