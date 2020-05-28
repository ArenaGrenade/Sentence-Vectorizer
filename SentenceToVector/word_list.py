class WFDict:
    def __init__(self, word=None, word_list=None):
        self.word_freq_dict = {}
        if word is not None:
            self.addWord(word)
        if word_list is not None:
            self.addListOfWords(word_list)

    def addWord(self, word):
        if word in self.word_freq_dict:
            self.word_freq_dict[word] += 1
        else:
            self.word_freq_dict[word] = 1

    def clearDictionary(self):
        self.word_freq_dict = {}

    def addListOfWords(self, list):
        for word in list:
            self.addWord(word)

    def getWordFreqDictionary(self):
        return self.word_freq_dict

    def getWordFrequency(self, word):
        return self.word_freq_dict[word]