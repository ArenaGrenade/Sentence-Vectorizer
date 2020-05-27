from nltk import pos_tag
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.wsd import lesk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


class BOWConvert:
    def __init__(self):
        self.punctuation = u",.?!()-_\"\'\\\n\r\t;:+*<>@#§^$%&|/"
        self.stopwords_en = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.tag_map = {"J": wordnet.ADJ,
                        "N": wordnet.NOUN,
                        "V": wordnet.VERB,
                        "R": wordnet.ADV}

    def convertWNPos(self, tag):
        # a helper function that return a corresponding element in the map, else just returns none
        return self.tag_map.get(tag[0].upper(), None)

    def lemmatize(self, wp_pair):
        # uses the helper function to get a conversion from the tree_bank tags to word-net tags
        pos_tag = self.convertWNPos(wp_pair[1])
        # Check if we get a pos_tag that is not none so that direct lemmatization works.
        # But if is just return the word alone.
        return self.lemmatizer.lemmatize(wp_pair[0], pos_tag) if pos_tag is not None else wp_pair[0]

    def convert(self, sentence):
        sentence_tokens = word_tokenize(sentence)  # tokenizing the sentence gives us a list of words
        tagged_tokens = pos_tag(sentence_tokens)  # tagging gives a (word, part of speech) tuple
        sentence_tokens = None  # cleaning up sentence tokens
        lemmas = [self.lemmatize(pair) for pair in
                  tagged_tokens]  # using the helper function we convert these words to lemmas
        tagged_tokens = None  # cleaning up tagged_tokens
        # this creates and initializes the bag of words and also cleans up the lemmas of some stop words and
        # removes punctuations and escape characters
        # this step also ensures all the words are in the same case so as to ensure uniformity
        bag = [w.lower() for w in lemmas if (w not in self.punctuation) and (w not in self.stopwords_en)]
        lemmas = None  # cleaning up the list of lemmas
        return bag
