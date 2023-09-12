# Simple topic labeling script using OpenAI API

I just wanted to test out the [OpenAI API](https://platform.openai.com/docs/introduction) by creating a little script for topic labeling. The script loads data from the `data` directory and extracts the positive and negative topics of the review in a comma-seperated-format.

## Usage

- Clone this repository
- Create a `.env` file in the root of the project and add your API key `OPENAI_API_KEY=<API-KEY>`

## Data

 I used a free [amazon dataset](https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/) for this. You can replace it with whatever you need. Just make the correct adjustments to the data loading functionality in `main.py`