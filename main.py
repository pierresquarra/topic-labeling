import gzip
import json
import os
import openai
import random
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def extract_topics(review):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a topic labeling assistant. Your task is to identify and categorize the topics "
                "discussed in the following review into two categories: positive topics and negative "
                "topics. Topics should be represented with a single word; if a topic can't be expressed "
                "with a single word, please omit it! List the topics in the following structured format: "
                "first, list all the positive topics separated by commas (if any), then a semicolon (;), "
                "followed by all the negative topics separated by commas (if any). There should always be "
                "a semicolon in your response to separate the two categories. \n\nFor example:\nservice,"
                "ambiance;pricey,portions\n\n",
            },
            {"role": "user", "content": "Great product and price!"},
            {"role": "assistant", "content": "product,price;\n\n"},
            {"role": "user", "content": "Bad customer support!"},
            {"role": "assistant", "content": ";support\n\n"},
            {"role": "user", "content": review},
        ],
    )
    print(response)
    return response


def parse(path):
    g = gzip.open(path, "r")
    for l in g:
        yield json.loads(l)


def print_reviews(data):
    for review in data:
        if "reviewText" in review:
            print(review["reviewText"])


if __name__ == "__main__":
    path = "data/AMAZON_FASHION_5.json.gz"
    data = parse(path)

    all_reviews = list(data)
    review = random.choice(all_reviews)["reviewText"]

    response = extract_topics(review)["choices"][0]["message"]["content"]

    positive_topics = response.split(";")[0].split(",")
    negative_topics = response.split(";")[1].split(",")

    print("Review: ", review)
    print("Positive topics: ", positive_topics)
    print("Negative topics: ", negative_topics)
