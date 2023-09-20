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
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a topic labeling assistant. Your task is to identify and categorize the topics "
                           "discussed in the reviews below into two categories: positive topics and negative topics. "
                           "Topics should be represented with a single word; if a topic can't be expressed with a "
                           "single word, please omit it! List the topics in the following structured format: first, "
                           "list all the positive topics separated by commas (if any), then a semicolon (;), "
                           "followed by all the negative topics separated by commas (if any). There should always be "
                           "a semicolon in your response to separate the two categories. For multiple reviews, "
                           "please separate the labels for each review with a \n delimiter."
            },
            {"role": "user", "content": "Great product and price!"},
            {"role": "assistant", "content": "product,price;\n\n"},
            {"role": "user", "content": "Bad customer support!"},
            {"role": "assistant", "content": ";support\n\n"},
            {"role": "user",
             "content": "The staff was very friendly and the food was out of this world. The ambiance of the restaurant was warm and welcoming. However, the prices were a bit steep and the wait time for the food was longer than expected."},
            {"role": "assistant", "content": "staff,food,ambience;prices,wait\n\n"},
            {"role": "user",
             "content": "Review 1: Great product and price\nReview 2: Bad customer support\nReview 3: The staff was very friendly and the food was out of this world. The ambiance of the restaurant was warm and welcoming. However, the prices were a bit steep and the wait time for the food was longer than expected."},
            {"role": "assistant", "content": "product,price;\n;support\nstaff,food,ambience;prices,wait\n\n"},
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
    batch_size = 5  # number of reviews to query from dataset

    all_reviews = list(data)
    reviews = random.sample(all_reviews, batch_size)
    reviews_str = "\n".join([f"Review {i + 1}: {review['reviewText']}" for i, review in enumerate(reviews)])

    response = extract_topics(reviews_str)["choices"][0]["message"]["content"]
    responses = response.split("\n")

    positive_topics = response.split(";")[0].split(",")
    negative_topics = response.split(";")[1].split(",")

    for i, resp in enumerate(responses):
        positive_topics = resp.split(";")[0].split(",")
        negative_topics = resp.split(";")[1].split(",")

        print(f"Review {i + 1}: ", reviews[i]["reviewText"])
        print("Positive topics: ", positive_topics)
        print("Negative topics: ", negative_topics)
