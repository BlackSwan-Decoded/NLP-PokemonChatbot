from contractions import expand_contractions
import nltk
import re
import unicodedata


def normalize_user_input(user_input):
    # replace contractions with full words
    message = expand_contractions(user_input).lower()
    print(message)
    # remove non-ascii characters
    message = unicodedata.normalize('NFKD', message).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    # remove punctuation
    message = re.sub(r'[^\w\s]', '', message)
    # tokenize
    message = nltk.word_tokenize(message)
    # remove stopwords
    # message = [word for word in message if word not in nltk.corpus.stopwords.words('english')]
    # lemmatize
    message = [nltk.stem.WordNetLemmatizer().lemmatize(word) for word in message]
    # remove single characters
    message = [word for word in message if (len(word) > 1 or word.isnumeric())]
    # remove words that are not in the rules.py dictionary
    # message = [word for word in message if word in rules.utterance_response]
    # return the normalized message
    return message
