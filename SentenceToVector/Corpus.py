class Corpus:
    def __init__(self):
        self.word_list = []

    def addWord(self, word):
        if word not in self.word_list:
            self.word_list.append(word)

    def addListOfWords(self, list):
        map(self.addWord, list)

    def getWordFreqTemplate(self):
        word_template_dict = {word: 0 for word in self.word_list}
        return word_template_dict
