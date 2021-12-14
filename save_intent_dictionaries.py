import json
import re

import pickle as pkl
from preprocess import normalize


with open('utterance_response.json') as file:
    data = json.load(file)


def save():
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

    utterance_patterns = open("utterance_patterns.pkl", "wb")
    response_patterns = open("response_patterns.pkl", "wb")
    pkl.dump(keywords_dict, utterance_patterns)
    pkl.dump(responses_dict, response_patterns)


def main():
    save()


if __name__ == '__main__':
    main()
