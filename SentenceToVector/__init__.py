from nltk import data, download
for download_package in ['wordnet', 'averaged_perceptron_tagger', 'punkt', 'stopwords']:
    try:
        data.find('tokenizers/'+download_package)
    except LookupError:
        download(download_package)

from .bag_of_words_converter import BOWConvert
from .tokens_to_vec import *
from .dataset_format_helper import *

sentence_tokenizer = data.load('tokenizers/punkt/english.pickle')
