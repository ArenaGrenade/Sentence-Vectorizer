def calculateTFDict(word_freq_dict, bag_of_words):
    tf_dict = {}
    num_of_bog = len(bag_of_words)
    for word, freq in word_freq_dict.items():
        tf_dict[word] = freq / float(num_of_bog)
    return tf_dict
