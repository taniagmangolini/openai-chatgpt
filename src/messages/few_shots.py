capitalize_task = [
    {
        "role": "user",
        "content": "electrons dance the tango of uncertainty,"
        "entangling bits in a choreography that outpaces"
        "the swiftest supercomputers.",
    },
    {
        "role": "assistant",
        "content": "Electrons Dance the Tango of Uncertainty, "
        "Entangling Bits in a Choreography That Outpaces "
        "the Swiftest Supercomputers.",
    },
    {
        "role": "user",
        "content": "cloud architectures whisper across the sky, "
        "weaving a tapestry of data that blankets the digital "
        "landscape in a seamless symphony of bytes.",
    },
    {
        "role": "assistant",
        "content": "Cloud Architectures Whisper Across the Sky, "
        "Weaving a Tapestry of Data That Blankets the Digital "
        "Landscape in a Seamless Symphony of Bytes.",
    },
    {
        "role": "user",
        "content": "artificial Intelligence, the alchemist of the digital "
        "age, transmutes raw data into a golden labyrinth of "
        "insights, charting new territories in the realm of "
        "human thought.",
    },
    {
        "role": "assistant",
        "content": "Artificial Intelligence, the Alchemist of the Digital "
        "Age, Transmutes Raw Data Into a Golden Labyrinth of "
        "Insights, Charting New Territories in the Realm of "
        "Human Thought.",
    },
    {
        "role": "user",
        "content": "the internet of things is a vast ocean of data, "
        "a sea of information that ebbs and flows "
        "with the tides of time.",
    },
]


format_numbers_task = [
    {
        "role": "user",
        "content": "Return a JSON containing " "the primary numbers between 0 and 7.",
    },
    {
        "role": "assistant",
        "content": """       
      {
        "data": [2, 3, 5, 7],
        "length": 4,
        "smallest": 2,
        "largest": 7,
      }
    """,
    },
    {
        "role": "user",
        "content": "Return a JSON containing " "the primary numbers between 0 and 6.",
    },
    {
        "role": "assistant",
        "content": """       
      {
        "data": [2, 3, 5],
        "length": 3,
        "smallest": 2,
        "largest": 5,
      }
    """,
    },
    {
        "role": "user",
        "content": "Return a JSON containing " "the primary numbers between 11 and 65.",
    },
]


# In this example, the model continues the list by adding the next item after the number 1 (prefix).
prefix = "\n\n1. "
seven_wonders_of_world_task = [
    {"role": "user", "content": f"What are the 7 wonders of the world?{prefix}"},
]


sci_fi_movies_2021 = [
    {"role": "user", "content": "Name sci-fi movies that came out in 2021."},
    {
        "role": "system",
        "content": """
    1. Dune
    2. Finch
    3. The Awake
    4. The Matrix Resurrections
    5. Mother/Android
    6. Bliss
    7. Swan Song
    """,
    },
    {"role": "user", "content": "Name fantasy movies that came out in 2021."},
]


def get_messages_for_generate_keywords_from_text_task(text):
    return [
    {
        "role": "system",
        "content": "You are a helpful bot that helps "
        "people extract keywords from a text."
        "Keywords are words that are important "
        "in a text.",
    },
    {
        "role": "user",
        "content": "In a whimsical town, old tortoise Orion "
        "scattered sunflower seeds atop a hill, "
        "believing they carried wishes to the stars. "
        "Unknown to him, children below rejoiced, "
        "believing these seeds were blessings from "
        "the sky. Sometimes, simple acts create magic.",
    },
    {
        "role": "assistant",
        "content": '["whimsical town", "old tortoise",'
        '"Orion", "sunflower seeds",'
        '"hill", "wishes", "stars", '
        '"children", "blessings", "sky",'
        '"simple acts", "magic"]',
    },
    {
        "role": "user",
        "content": "In the world of quantum computing, the Hadron "
        "Processing Unit (HPU) stands out. Utilizing "
        "qubit superposition, it offers exceptional "
        "speeds. Paired with nanophotonic circuits, "
        "it ensures fast qubit communication, while "
        "quantum tunneling aids in error correction. "
        "With quantum annealing algorithms, the HPU "
        "brings us closer to achieving quantum supremacy.",
    },
    {
        "role": "assistant",
        "content": '["quantum computing", "Hadron Processing Unit", '
        '"HPU", "qubit superposition", "speeds",  '
        '"nanophotonic circuits", "qubit communication",  '
        '"quantum tunneling", "error correction",  '
        '"quantum annealing algorithms",  '
        '"quantum supremacy"] ',
    },
    {
        "role": "user",
        "content": text
    },
]


def get_messages_for_generate_hashtags_from_text_task(text):
    return [
        {
            "role": "system",
            "content": "You are a helpful bot that helps people "
            "extract hashtags from text to use them "
            "on Twitter.",
        },
        {
            "role": "user",
            "content": "In a whimsical town, old tortoise Orion "
            "scattered sunflower seeds atop a hill, "
            "believing they carried wishes to the "
            "stars. Unknown to him, children below "
            "rejoiced, believing these seeds were "
            "blessings from the sky. Sometimes, "
            "simple acts create magic.",
        },
        {
            "role": "assistant",
            "content": "#Wishes #Blessings  #Magic",
        },
        {
            "role": "user",
            "content": "In the world of quantum computing, "
            "the Hadron Processing Unit (HPU) "
            "stands out. Utilizing qubit superposition, "
            "it offers exceptional speeds. Paired with "
            "nanophotonic circuits, it ensures fast qubit "
            "communication, while quantum tunneling aids "
            "in error correction. With quantum annealing "
            "algorithms, the HPU brings us closer to "
            "achieving quantum supremacy.",
        },
        {
            "role": "assistant",
            "content": "#QuantumComputing #Qubit #QuantumAlgorithms",
        },
        {
            "role": "user",
            "content": "What makes a good friend is someone who is "
            "there for you when you need them. They are "
            "someone who will listen to your problems "
            "and help you find solutions. They are "
            "someone who will be there for you "
            "when you need them most.",
        },
        {
            "role": "assistant",
            "content": "#Friendship #FriendshipQuotes #Support",
        },
        {"role": "user", "content": text },
    ]


def get_messages_for_tweet_generation_task(text, hashtags):
    return [
        {
            "role": "system",
            "content": "You are an intelligent assistant that assists "
            "users in creating a tweet with hashtags based "
            "on a given text. The tweet should be between "
            "100 and 280 characters in length.",
        },
        {
            "role": "user",
            "content": "OpenAI has been pushing the boundaries of large "
            "language models, making them more accessible to "
            "the public and businesses alike. The models can "
            "generate human-like text, assist in writing, "
            "answer questions, and more. "
            "#OpenAI #AI #LanguageModels",
        },
        {
            "role": "assistant",
            "content": "OpenAI advances large language models for public "
            "and business use. They generate human-like text, "
            "assist writing, and answer questions. "
            "#OpenAI #AI #LanguageModels",
        },
        {
            "role": "user",
            "content": "The Eiffel Tower, located in Paris, France, "
            "is a world-renowned architectural marvel and "
            "a symbol of love. Many tourists visit it annually "
            "to witness its grandeur and romantic ambiance. "
            "#EiffelTower #Paris #Romance",
        },
        {
            "role": "assistant",
            "content": "Paris's Eiffel Tower is an iconic symbol of love, "
            "drawing tourists worldwide to its majestic "
            "presence. "
            "#EiffelTower #Paris #Love",
        },
        {
            "role": "user",
            "content": "Yoga is an ancient practice originating from India. "
            "It focuses on mental, physical, and spiritual "
            "well-being, offering exercises and meditations "
            "that promote holistic health. "
            "#Yoga #Wellness #Meditation",
        },
        {
            "role": "assistant",
            "content": "Yoga, from India, balances mind, body, and spirit "
            "through exercises and meditation. "
            "#Yoga #HolisticHealth #Meditation",
        },
        {
            "role": "user",
            "content": "Pandas are native to South Central China and are known "
            "for their distinct black and white appearance. They "
            "mostly eat bamboo and are a symbol of peace and "
            "conservation efforts. "
            "#Pandas #China #Conservation",
        },
        {
            "role": "assistant",
            "content": "Native to China, pandas with their iconic black and "
            "white look are symbols of peace and conservation. "
            "#Pandas #China #Peace",
        },
        {
            "role": "user",
            "content": "The Grand Canyon is a steep-sided canyon carved by "
            "the Colorado River in the U.S. state of Arizona. "
            "It's one of the most famous landmarks and is known "
            "for its immense size and its intricate and colorful "
            "landscape. "
            "#GrandCanyon #Arizona #Nature",
        },
        {
            "role": "assistant",
            "content": "The Grand Canyon, carved by the Colorado River in "
            "Arizona, is famous for its immense size and colorful "
            "landscape. "
            "#GrandCanyon #Arizona #Nature",
        },
        {"role": "user", "content": f"{text}. {hashtags}"},
    ]
