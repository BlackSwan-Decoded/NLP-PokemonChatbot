utterance_response = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"hi|hey|hello|howdy|sup|wassup",
        ["Hello", "Hey there", "Hi", ]
    ],
    [
        r"what is your name",
        ["My name is PokeBot! ", ]
    ],
    [
        r"how are you",
        ["I'm doing good.\nHow about You?", ]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind", ]
    ],
    [
        r"i am fine|i am (.*) doing good",
        ["Great to hear that, How can I help you?", "Nice to hear that, How can I help you? :)", ]
    ],
    [
        r"(.*) age",
        ["I'm a computer program. I have no idea ;)", ]
    ],
    [
        r"(.*) created",
        ["Swanora created me using Python's NLTK library ", "top secret ;)", ]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"i want to know about (.*) | tell me about (.*) | which pokemon is (.*)",
        ["Here's what I know about %1: ", "Alright, %1 is: "]
    ],
]
