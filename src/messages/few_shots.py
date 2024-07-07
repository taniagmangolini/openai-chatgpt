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


keywords_task = [
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
        "content": "The first programming language to be invented was "
        "Plankalkül, which was designed by Konrad Zuse in "
        "the 1940s, but not publicly known until 1972 "
        "(and not implemented until 1998). The first "
        "widely known and successful high-level programming "
        "language was Fortran, developed from 1954 to 1957 "
        "by a team of IBM researchers led by John Backus. "
        "The success of FORTRAN led to the formation of a "
        'committee of scientists to develop a "universal" '
        "computer language; the result of their effort was "
        "ALGOL 58. Separately, John McCarthy of MIT developed "
        "Lisp, the first language with origins in academia "
        "to be successful. With the success of these initial "
        "efforts, programming languages became an active "
        "topic of research in the 1960s and beyond.",
    },
]
