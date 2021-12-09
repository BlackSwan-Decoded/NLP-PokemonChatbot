from normalize import normalize_user_input
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import rules


def get_input():
    print("Welcome to the Pokemon Chatbot!")
    print("Please enter a question or type 'quit' to exit.")
    return input(">> ")


def main():
    user_input = get_input()
    norm_input = normalize_user_input(user_input)
    print(norm_input)


if __name__ == '__main__':
    main()
