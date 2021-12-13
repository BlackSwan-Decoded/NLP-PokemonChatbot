import re
import pandas as pd
import preprocess as norm
import pypokedex as pdx
import long_responses as long


pokemon_df = pd.read_csv('pokemon.csv')
pokemon_names = [name.lower() for name in pokemon_df['NAME']]


def message_probability(user_message, recognised_words, single_response=False, required_words=None):
    if required_words is None:
        required_words = []
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    # If the message contains all the required words, it will be given a higher probability
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the accuracy percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    # Prevents the bot from wrongly matching sentence if the required words are not present
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # If the message contains all the required words, it will be given a higher probability
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}
    for word in message:
        if word in pokemon_names or word.isnumeric():
            message.append("pokemon")
            break

    # Simplifies response creation / adds it to the dict
    # Assigns a probability to each message
    def response(bot_response, list_of_words, single_response=False, required_words=None):
        if required_words is None:
            required_words = []
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response(["Hello", "Hey there", "Hi"], ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Ok', ['tell', 'about', 'pokemon'], required_words=['pokemon'])

    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])


    # gets the highest probability response
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    if best_match == 'Ok':
        pokemon = ""
        for word in message:
            if word in pokemon_names or word.isnumeric():
                pokemon = word

        pokemon = pdx.get(name=pokemon)
        return pokemon.name

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    norm_input = norm.normalize_user_input(user_input)
    print(norm_input)
    response = check_all_messages(norm_input)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))