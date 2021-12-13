import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response


"""Dictionary of intents with tags as keys and dictionaries of intents as values.
   Value dictionaries contain the following keys: utterances and responses which
   corresponds to a list of utterance patterns and responses respectively. """
utterance_response = {
    "greeting": {
        "utterances": [r"hi|hey|hello|hey there, howdy|sup|wassup"],
        "responses": [
            "Hey there!",
            "Hi!",
            "Hello!",
            "Hello,"
            "Thanks for stopping by"
        ]
    },
    "goodbye": {
        "utterances": [r"bye|goodbye|see you later|see you|see ya|catch ya|catch you later|quit|quit talking|quit "
                       r"talking to me"],
        "responses": [
            "Bye!",
            "Goodbye!",
            "See you later!",
            "Bye take care. See you soon :) ",
            "It was nice talking to you. See you soon :)"
        ]
    },
    "thanks": {
        "utterances": [r"thanks|thank you|thank you so much|that's very kind of you|that's helpful|that's very helpful"],
        "responses": [
            "You're welcome!",
            "No problem!",
            "You're welcome!",
            "Any time!",
            "My pleasure!"
        ]
    },
    "name": {
        "utterances": [r"my name is (.*)|i am (.*)|i'm (.*)|i am called (.*)|i'm called (.*)"],
        "responses": [
            "Nice to meet you %1",
            "Hi %1",
            "Nice to meet you %1, which pokemon do you want to know about?",
            "Hi %1, which pokemon do you want to know about?"
        ]
    },
    "pokemon": {
        "utterances": [
            r"which pokemon is (*)|what is (*)|tell me about (*)|i want to know about (.*)|i want to know more about "
            r"(.*)"],
        "responses": [
            "Here's what I know about %1",
            "Alright, here's what I know about %1",
            "Alright, %1 is",
            "No problem! Let me get that for you",
            "%1 is"
        ]
    }
}

utterances = {"greeting": utterance_response["greeting"]["utterances"],
              "goodbye": utterance_response["goodbye"]["utterances"],
              "thanks": utterance_response["thanks"]["utterances"],
              "name": utterance_response["name"]["utterances"],
              "pokemon": utterance_response["pokemon"]["utterances"]}

responses = {"greeting": utterance_response["greeting"]["responses"],
             "goodbye": utterance_response["goodbye"]["responses"],
             "thanks": utterance_response["thanks"]["responses"],
             "name": utterance_response["name"]["responses"],
             "pokemon": utterance_response["pokemon"]["responses"]}

print(utterances)
print(responses)
