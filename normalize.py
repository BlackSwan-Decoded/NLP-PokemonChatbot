from contractions import expand_contractions
import nltk
import numpy as np
import re
import unicodedata

ignore = ['?', '!', ',', '.', ';', '(', ')', '[', ']', '{', '}', '<', '>', '+', '-', '*', '/', '=', '&', '|', '^', '%',
          '$', '#', '@', '~', '`', '!', '_', '\\', '\'', '\"']


def tokenize(sentence):
    # replace contractions with full words
    message = expand_contractions(sentence).lower()
    # message = user_input.lower()what's
    # remove non-ascii characters
    message = unicodedata.normalize('NFKD', message).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    # remove punctuation
    remove_punctuation(message)
    return nltk.word_tokenize(message)

def remove_punctuation(normalized_message):
    re.sub(r'[^\w\s]', '', normalized_message)


def remove_stop_words(normalized_message):
    return [word for word in normalized_message if word not in nltk.corpus.stopwords.words('english')]


def lemmatize(normalized_sentence):
    return [nltk.stem.WordNetLemmatizer().lemmatize(word) for word in normalized_sentence]


def stem(normalized_message):
    return [nltk.stem.PorterStemmer().stem(word) for word in normalized_message]


def remove_single_characters(normalized_sentence):
    return [word for word in normalized_sentence if (len(word) > 1 or word.isnumeric())]


def normalize_user_input(user_input):
    # tokenize
    message = tokenize(user_input)
    # remove stopwords
    message = remove_stop_words(message)
    # lemmatize
    message = lemmatize(message)
    # stem
    message = stem(message)
    # remove single characters
    message = remove_single_characters(message)
    # remove words that are not in the rules.py dictionary
    # message = [word for word in message if word in rules.utterance_response]
    # return the normalized message
    return message


def normalize(tokenized_sentence):
    message = lemmatize(tokenized_sentence)
    message = stem(message)
    return remove_single_characters(message)


def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1

    return bag
