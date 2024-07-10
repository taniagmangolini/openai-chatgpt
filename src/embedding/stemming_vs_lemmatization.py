import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download("wordnet")
nltk.download("omw-1.4")

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# List of words to process
words = ["running", "runner", "jumps", "easily", "better"]

# Stemming process
stemmed_words = [stemmer.stem(word) for word in words]

# Lemmatization process with POS specification
# (POS: Part of Speech)
lemmatized_words = []
for word in words:
    # Default to noun
    pos_tag = "n"
    if word in ["better"]:
        # Treat this example as an adjective
        pos_tag = "a"
    elif word in ["running", "jumps"]:
        # Treat these examples as verbs
        pos_tag = "v"
    elif word in ["easily"]:
        # Treat this example as an adverb
        pos_tag = "r"
    else:
        # Treat all other examples as nouns
        pos_tag = "n"
    lemmatized_word = lemmatizer.lemmatize(word, pos=pos_tag)
    lemmatized_words.append(lemmatized_word)

# Print results
print("Original: ", words)
print("Stemmed: ", stemmed_words)
print("Lemmatized: ", lemmatized_words)
