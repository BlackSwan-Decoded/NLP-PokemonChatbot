from contractions import expand_contractions
import nltk
import numpy as np
import re
import unicodedata


def tokenize(sentence):
    # replace contractions with full words
    sentence = expand_contractions(sentence)
    # remove non-ascii characters
    sentence = unicodedata.normalize('NFKD', sentence).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    # remove punctuation
    remove_punctuation(sentence)
    # tokenize into words
    return nltk.word_tokenize(sentence)


def expand_sentence(sentence):
    return expand_contractions(sentence).lower()


def remove_punctuation(sentence):
    re.sub(r'[^\w\s]', '', sentence)


def remove_stop_words(sentence):
    return [word for word in sentence if word not in nltk.corpus.stopwords.words('english')]


def lemmatize(sentence):
    return [nltk.stem.WordNetLemmatizer().lemmatize(word) for word in sentence]


def stem(sentence):
    return [nltk.stem.PorterStemmer().stem(word) for word in sentence]


def remove_single_characters(sentence):
    return [word for word in sentence if (len(word) > 1 or word.isnumeric())]


def normalize(sentence):
    # tokenize message
    words = tokenize(sentence.lower())
    # remove stopwords
    words = remove_stop_words(words)
    # lemmatize
    words = lemmatize(words)
    # stem
    words = stem(words)
    # remove single characters
    words = remove_single_characters(words)
    # return the normalized message
    return words


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
