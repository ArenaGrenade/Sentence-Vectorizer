from . import sentence_tokenizer


def convertDocToSentences(document):
    """
    This function takes in a string which can contain end of line escape characters, but the tokenizer cleans that up
    and returns a list of sentences. No punctuation is removed. This can be taken care of by other utilities.
    :param document: a string containing all sentences which maybe organized into paragraphs
    :return: a list of all sentences present in the given document
    """

    return sentence_tokenizer.tokenize(document)


def convertSentencesToListOfWords(sentence_list, bow_converter_obj):
    """
    Given a list of sentences and a Bag Of Words constructor this functions returns tokenized versions of all words
    present in all the sentences provided.

    :param sentence_list: a list containing all the sentences to be processed
    :param bow_converter_obj: an object of type BOWConvert
    :return: a list of words present in all the sentences
    """

    return [word for sentence in sentence_list for word in bow_converter_obj.convert(sentence)]


def convertSentencesToListOfTokens(sentence_list, bow_converter_obj):
    """
    Given a list of sentences and a Bag Of Words constructor this functions returns tokenized versions of these
    sentences as a 2-D list of tokens. Each element in the returned list is a list of tokens present in the
    corresponding tokens.

    :param sentence_list: a list containing all the sentences to be processed
    :param bow_converter_obj: an object of type BOWConvert
    :return: 2-D list of tokens of sentences provided
    """

    return [bow_converter_obj.convert(sentence) for sentence in sentence_list]


def convertListOfSentenceTokensToListOfWords(matrix_of_tokens):
    """
    Given a 2-D matrix of tokens with each 1-D list in the matrix representing a list of tokens of a single sentence,
    this function converts it to a flattened 1-D representation of all the tokens in the matrix.

    :param matrix_of_tokens: 2-D list of tokens
    :return: 1-D list of tokens
    """

    return [token for sentence_of_tokens in matrix_of_tokens for token in sentence_of_tokens]
