def get_sentiment(text_to_analyze, gcp_language_client):
    """
    Uses the Google Natural Language API to analyze sentiment of
    input.
    """
    # language not explicitly set, so API will auto-detect
    document = types.Document(
        content = text_to_analyze,
        type = enums.Document.Type.PLAIN_TEXT
        )
    sentiment = gcp_language_client.analyze_sentiment(
        document=document).document_sentiment
    sentiment_dict = {}
    sentiment_dict[‘magnitude’] = sentiment.magnitude
    sentiment_dict[‘score’] = sentiment.score
    return sentiment_dict

    import argparse

from google.cloud import language_v1

def print_result(annotations): score = annotations.document_sentiment.score magnitude = annotations.document_sentiment.magnitude

def analyze(movie_review_filename): """Run a sentiment analysis request on text within a passed filename.""" client = language_v1.LanguageServiceClient()

if name == "main": parser = argparse.ArgumentParser( description=doc, formatter_class=argparse.RawDescriptionHelpFormatter ) parser.add_argument( "movie_review_filename", help="The filename of the movie review you'd like to analyze.", ) args = parser.parse_args()