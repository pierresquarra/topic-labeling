# Simple topic labeling script using OpenAI API

I wanted to test out the [OpenAI API](https://platform.openai.com/docs/introduction) by creating a little script for topic labeling. The script loads data from the `data` directory and extracts the positive and negative topics of the review in a comma-seperated-format.

**Important note:** The script works best with *gpt-4*. When using *gpt-3.5-turbo*, the semicolon separating the good from the bad topics is not always provided. Errorhandling for this can easily be implemented though. The *average number of tokens* used with gpt-3.5-turbo is 200 tokens.

## Usage

- Clone this repository
- Create a `.env` file in the root of the project and add your API key `OPENAI_API_KEY=<API-KEY>`

## Data

 I used a free [amazon dataset](https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/) for this. You can replace it with whatever you need. Just make the correct adjustments to the data loading functionality in `main.py`

 ## Example

 When running the script for the first review of the data set *Great product and price!*, the positive topics are *['product', 'price]* and the negative topics are *['']*.

## Improvements

- Handle multiple reviews in one prompt for token efficiency
- The prompt needs much more specification (type of reviews, products that the review was written for, etc.)
