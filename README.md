# Prompt Engineering with Python and OpenAI API

## Prompt engineering techniques

OpenAI GPT For Python Developers (Aymen El Amri), by Packt Publishing.

Some prompt engineering techniques:

- Zero-shot learning: prompting an LLM without any examples.
- Few-shot learning: prompting an LLM with examples of task.
- General knowledge prompting: ask the LLM to generate useful information about a given topic before generating a final response.
- Chain of Thought (CoT): Shows the LLM examples of logical reasoning to approach a solution to instruct it to follow a similar m ethod of reasoning in its response.
- Zero-shot CoT
- Auto Chain of Thought (AutoCoT)
- Self-consistency
- Transfer Learning, ReAct (Reason + Act)
- Others

## Embedding

Embeddings represent real-world objects and relationships in the form of vectors that measures the similarity between two entities.

 Text embeddings represent text strings as vectors, enabling the measurement of similarity between them with the intention of finding the most relevant results for a search query (Search), grouping text strings based on their similarity (clustering), recommending items with similar text (recommendation), identifying text strings that greatly differ from others (anomaly detector), analyzing the differences between text strings (diversity), and labeling text strings based on their closest match (classification).

 “Ada” is one of the best models available on OpenAI for embedding.
 

# Environment

Create an API key on https://platform.openai.com/api-keys and place it in an .env file on the src folder with the API_KEY and ORG_ID.

```
# Install the dependencies and the env variables
pip install --upgrade pip
pip install virtualenv
pip3 install virtualenvwrapper

export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=$(which python3)
source /usr/local/bin/virtualenvwrapper.sh
source ~/.bashrc

# To create the env
mkvirtualenv -p /usr/bin/python3.9 openaigptforpythondevelopers

# To activate
workon openaigptforpythondevelopers

# To deactivate
deactivate
```

# Running the scripts

```
python -m chat.chat_completion

python -m embedding.first_embedding
```
