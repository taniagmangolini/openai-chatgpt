capitalize_task = [
  {
    "role": "user", 
    "content":
      "electrons dance the tango of uncertainty,"
      "entangling bits in a choreography that outpaces"
      "the swiftest supercomputers."
  },
  {
    "role": "assistant",
    "content": 
      "Electrons Dance the Tango of Uncertainty, "
      "Entangling Bits in a Choreography That Outpaces "
      "the Swiftest Supercomputers."
  },
  {
    "role": "user",
    "content":
      "cloud architectures whisper across the sky, "
      "weaving a tapestry of data that blankets the digital "
      "landscape in a seamless symphony of bytes."
  },
  {
    "role": "assistant",
    "content":
      "Cloud Architectures Whisper Across the Sky, " 
      "Weaving a Tapestry of Data That Blankets the Digital "
      "Landscape in a Seamless Symphony of Bytes."
  },
  {
    "role": "user",
    "content":
      "artificial Intelligence, the alchemist of the digital "
      "age, transmutes raw data into a golden labyrinth of "
      "insights, charting new territories in the realm of "
      "human thought."
  },
  {
    "role": "assistant",
    "content":
      "Artificial Intelligence, the Alchemist of the Digital "
      "Age, Transmutes Raw Data Into a Golden Labyrinth of "
      "Insights, Charting New Territories in the Realm of "
      "Human Thought."
  },
  {
    "role": "user",
    "content":
      "the internet of things is a vast ocean of data, "
      "a sea of information that ebbs and flows "
      "with the tides of time."
  }
]


format_numbers_task = [
  {
    "role": "user", 
    "content": 
      "Return a JSON containing " 
      "the primary numbers between 0 and 7."
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
    """
  },
  {
    "role": "user", 
    "content": 
      "Return a JSON containing "
      "the primary numbers between 0 and 6."
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
    """
  },
  {
    "role": "user", 
    "content": 
      "Return a JSON containing "
      "the primary numbers between 11 and 65."
  }
]


# In this example, the model continues the list by adding the next item after the number 1 (prefix).
prefix = "\n\n1. "
seven_wonders_of_world_task = [
  {
    "role": "user", 
    "content": 
      f"What are the 7 wonders of the world?{prefix}"
  },
]
