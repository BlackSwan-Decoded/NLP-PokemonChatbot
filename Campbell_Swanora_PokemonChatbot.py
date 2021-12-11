from normalize import normalize_user_input
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
import pandas as pd
import rules


def get_input():
    print("Welcome to the Pokemon Chatbot!")
    print("Please enter a question or type 'quit' to exit.")
    return input(">> ")


def main():
    user_input = get_input()
    norm_input = normalize_user_input(user_input)
    norm_input = pd.DataFrame({"Input": norm_input})
    get_response(norm_input)


def get_response(df):
    stop_words = 'english'
    max_df = 1.0
    min_df = 0.0
    df = df.Input
    t_vect = TfidfVectorizer(stop_words=stop_words, max_df=max_df, min_df=min_df)
    tdif_transformation = t_vect.fit_transform(df)
    tdif_features = t_vect.get_feature_names_out()

    vals = cosine_similarity(tdif_transformation[-1], tdif_transformation)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if(req_tfidf == 0):
        print("Sorry, I don't understand.")
        return
    else:
        print(df[idx])
        return


if __name__ == '__main__':
    main()
