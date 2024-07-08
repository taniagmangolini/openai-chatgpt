# Prompt Engineering with Python and OpenAI API

Studies related to the book:

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


# Environment

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
