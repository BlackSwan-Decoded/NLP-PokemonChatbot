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
pokemon_df = pd.read_csv('pokemon.csv')
pokemon_names = [name.lower() for name in pokemon_df['NAME']]


def pokebot():
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
            print(user_input)

            if key == 'goodbye':
                print(random.choice(responses[key]))
                exit()

            if key == 'name':
                print(f'{random.choice(responses[key])} {user_input[1].title()}!')
            elif key == 'pokemon':
                print(random.choice(responses[key]))
                getPokemon(pokemon_name)
            else:
                print(random.choice(responses[key]))

        else:
            print("Sorry, I don't understand")


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
            return random.choice(responses[key])
            # exit()

        if key == 'name':
            return f'{random.choice(responses[key])} {user_input[1].title()}!'
        elif key == 'pokemon':
            return random.choice(responses[key])
            getPokemon(pokemon_name)
        else:
            return random.choice(responses[key])

    return "Sorry, I don't understand"


def getPokemon(pokemon_name):
    try:
        pokemon = pdx.get(name=pokemon_name)
        print(f'>> Your pokemon is {pokemon.name.title()}!')
        print(f'>> ' + pokemon.description)
        print(f'>> Type: {pokemon.types[0].name}')
        print(f'>> Height: {pokemon.height}')
        print(f'>> Weight: {pokemon.weight}')
        print(f'>> Base experience: {pokemon.base_experience}')
        print(f'>> Abilities: {pokemon.abilities[0].name}')
        print(f'>> Stats: {pokemon.stats[0].name}')
        print(f'>> Stats: {pokemon.stats[1].name}')
        print(f'>> Stats: {pokemon.stats[2].name}')
        print(f'>> Stats: {pokemon.stats[3].name}')
        print(f'>> Stats: {pokemon.stats[4].name}')
        print(f'>> Stats: {pokemon.stats[5].name}')
        print(f'>> Stats: {pokemon.stats[6].name}')
    except:
        print("\tSorry, I don't know that Pokemon.")


def main():
    print("Welcome to pokeBot!")
    print("Let's talk about your Pokemon!")


if __name__ == "__main__":
    main()
