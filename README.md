# EC601-Project2
EC602 Project2 for Google NLP
"""Demonstrates how to make a simple call to the Natural Language API."""


import argparse

from google.cloud import language_v1





def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude








def analyze(movie_review_filename):
    """Run a sentiment analysis request on text within a passed filename."""
    client = language_v1.LanguageServiceClient()

  






if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "movie_review_filename",
        help="The filename of the movie review you'd like to analyze.",
    )
    args = parser.parse_args()

  


#tests and results 
#the coding part is searched from web. I tried to understand the all steps. BY reading the assignments, I find some tests parts for google NLP. Some Results look good, but some parts are not good enough to pass the test. 
