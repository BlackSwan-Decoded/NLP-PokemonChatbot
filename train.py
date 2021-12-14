import json
import re
import pandas as pd
from preprocess import normalize
import pypokedex as pdx
import random

with open('utterance_response.json') as file:
    data = json.load(file)

pokemon_df = pd.read_csv('pokemon.csv')
pokemon_names = [name.lower() for name in pokemon_df['NAME']]


def bot(utterances, responses):
    while True:
        pokemon_name = ""
        user_input = normalize(input("You >> "))
        matched_intent = None

        for intent, pattern in utterances.items():
            for word in user_input:
                if re.search(pattern, word):
                    matched_intent = intent
                    break

        if (matched_intent is None) or (matched_intent == 'pokemon'):
            for word in user_input:
                if word in pokemon_names or word.isnumeric():
                    pokemon_name = word
                    matched_intent = 'pokemon'
                    break

        if matched_intent in responses:
            key = matched_intent
            print(random.choice(responses[key]))

            if key == 'pokemon':
                try:
                    pokemon = pdx.get(name=pokemon_name)
                    print(f"PokeBot >> Your pokemon is {pokemon.name.title()}!")
                except:
                    print("\tSorry, I don't know that Pokemon.")

        else:
            print("Sorry, I don't understand")


def train():
    intents = {}
    keywords_dict = {}
    responses_dict = {}

    for intent in data['utterance_response']:
        tag = intent['tag']
        intents[tag] = []
        responses_dict[tag] = intent['responses']
        for pattern in intent['patterns']:
            pattern = [f'.*\\b{pat}\\b.*' for pat in normalize(pattern)]
            intents[tag].extend([pat for pat in pattern if pat not in intents[tag]])
    for intent, keys in intents.items():
        keywords_dict[intent] = re.compile('|'.join(keys))
    return keywords_dict, responses_dict


def main():
    print("Welcome to pokeBot!")
    print("Let's talk about your Pokemon!")
    utt, resp = train()
    bot(utt, resp)


if __name__ == "__main__":
    main()
