"""Dictionary of intents with tags as keys and dictionaries of intents as values.
   Value dictionaries contain the following keys: utterances and responses which
   corresponds to a list of utterance patterns and responses respectively. """
utterance_response = {
    "greeting": {
        "utterances": [
            "hi",
            "hey",
            "hello",
            "hey there",
            "howdy",
            "sup",
            "wassup",
            "what's up",
            "what's good"
        ],
        "responses": [
            "Hey there!",
            "Hi!",
            "Hello!",
            "Hello,"
            "Thanks for stopping by"
        ]
    },
    "goodbye": {
        "utterances": [
            "bye",
            "goodbye",
            "see you later",
            "see you",
            "see ya",
            "catch ya",
            "catch you later",
            "quit",
            "quit talking",
            "quit talking to me"
        ],
        "responses": [
            "Bye!",
            "Goodbye!",
            "See you later!",
            "Bye take care. See you soon :) ",
            "It was nice talking to you. See you soon :)"
        ]
    },
    "thanks": {
        "utterances": [
            "thanks",
            "thank you",
            "thank you so much",
            "that's very kind of you",
            "that's helpful",
            "that's very helpful"
        ],
        "responses": [
            "You're welcome!",
            "No problem!",
            "You're welcome!",
            "Any time!",
            "My pleasure!"
        ]
    },
    "name": {
        "utterances": [
            r"my name is (.*)",
            r"i am (.*)",
            r"i'm (.*)",
            r"i am called (.*)",
            r"i'm called (.*)"
        ],
        "responses": [
            "Nice to meet you %1",
            "Hi %1",
            "Nice to meet you %1, which pokemon do you want to know about?",
            "Hi %1, which pokemon do you want to know about?"
        ]
    },
    "pokemon": {
        "utterances": [
            r"which pokemon is (*)",
            r"what is (*)",
            r"tell me about (*)",
            r"i want to know about (.*)",
            r"i want to know more about (.*)"
        ],
        "responses": [
            "Here's what I know about %1",
            "Alright, here's what I know about %1",
            "Alright, %1 is",
            "No problem! Let me get that for you",
            "%1 is"
        ]
    }
}
