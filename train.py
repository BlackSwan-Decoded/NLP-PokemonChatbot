import json
import re
import pandas as pd
from preprocess import normalize_user_input as normalize
import pypokedex as pdx


with open('utterance_response.json') as file:
    data = json.load(file)

pokemon_df = pd.read_csv('pokemon.csv')
pokemon_names = [name.lower() for name in pokemon_df['NAME']]
pokemon_name = ""

def bot(utterances, responses):
    global pokemon_name
    while True:
        user_input = input("You: ")
        user_input = user_input.lower()
        matched_intent = None

        for intent, pattern in utterances.items():
            if re.search(pattern, user_input):
                matched_intent = intent
                break
            else:
                user_input = normalize(user_input)
                for word in user_input:
                    if word in pokemon_names or word.isnumeric():
                        pokemon_name = word
                        matched_intent = 'pokemon'
                break

        if matched_intent in responses:
            key = matched_intent
            print(responses[key])

            if key == 'pokemon':
                pokemon = pdx.get(name=pokemon_name)
                print(pokemon.name)
        else:
            print("Sorry, I don't understand")


def train():
    intents = {}
    keywords_dict = {}
    responses_dict = {}

    for intent in data['utterance_response']:
        tag = intent['tag']
        intents[tag] = []
        for pattern in intent['patterns']:
            pattern = pattern.lower()
            pattern = normalize(pattern)
            intents[tag].extend('.*\\b'+pat+'\\b.*' for pat in pattern)
        for response in intent['responses']:
            responses_dict[tag] = response
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
