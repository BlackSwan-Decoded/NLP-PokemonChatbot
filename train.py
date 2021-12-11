import json
import normalize as norm
import numpy as np

with open('utterance_response.json') as file:
    data = json.load(file)

all_words = []
tags = []
docs_x = []
docs_y = []
xy = []

for intent in data['utterance_response']:
    tag = intent['tag']
    if tag not in tags:
        tags.append(intent['tag'])

    for pattern in intent['patterns']:
        words = norm.tokenize(pattern)
        all_words.extend(words)
        docs_x.append(words)
        docs_y.append(tag)
        xy.append((words, tag))

all_words = norm.normalize(all_words)
all_words = sorted(set(all_words))
tags = sorted(set(tags))
print(all_words)
# print(tags)

# X_train = []
# Y_train = []
# for (pattern_sentence, tag) in xy:
#     bag = norm.bag_of_words(pattern_sentence, all_words)
#     X_train.append(bag)
#     label = tags.index(tag)
#     Y_train.append(label)
#
# X_train = np.array(X_train)
# Y_train = np.array(Y_train)
