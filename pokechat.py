import random
import re

import pandas as pd
import pickle as pkl
import pypokedex as pdx

from preprocess import normalize

# Load data intents data
with open('utterance_patterns.pkl', 'rb') as utt_pkl:
    utterances = pkl.load(utt_pkl)
with open('response_patterns.pkl', 'rb') as resp_pkl:
    responses = pkl.load(resp_pkl)

# Get pokemon names from csv file found at https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6
bot_name = "PokeBot"
pokemon_df = pd.read_csv('pokemon.csv')
pokemon_names = [name.lower() for name in pokemon_df['NAME']]


def get_response(user_input):
    pokemon_name = ""
    matched_intent = None
    user_input = normalize(user_input)

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

        if key == 'goodbye':
            exit(random.choice(responses[key]))

        if key == 'name':
            return f"{random.choice(responses[key])} {user_input[1].title()}!"
        elif key == 'pokemon':
            pokemon_details = get_pokemon(pokemon_name)
            return f"{random.choice(responses[key])}\n{pokemon_details}"
        else:
            return random.choice(responses[key])

    return "Sorry, I do not understand"


def get_pokemon(pokemon_name):
    try:
        pokemon = pdx.get(name=pokemon_name)
        response = f"Meet {pokemon.name.title()}!" \
                   f"\n{pokemon.name.title()} has these attributes:" \
                   f"\nType: {pokemon.types[0].title()}!" \
                   f"\nHeight: {pokemon.height}!" \
                   f"\nWeight is {pokemon.weight}!" \
                   f"\nBase Experience is {pokemon.base_experience}!" \
                   f"\nAbilities are {pokemon.abilities[0].name, pokemon.abilities[1].name}!" \
                   f"\nStats are hp={pokemon.base_stats[0]}, attack={pokemon.base_stats[1]}, defense" \
                   f"={pokemon.base_stats[2]}, sp_atk={pokemon.base_stats[3]}, sp_def={pokemon.base_stats[4]}," \
                   f"speed={pokemon.base_stats[5]}"
    except:
        response = "\tSorry, I don't know that Pokemon."

    return response


def main():
    print(f"Hi! I'm {bot_name}!")
    while True:
        user_input = input("\nWhat would you like to know?\n")
        response = get_response(user_input)
        print(response)


if __name__ == "__main__":
    main()
