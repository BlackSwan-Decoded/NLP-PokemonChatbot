from contractions import expand_contractions

import nltk
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
