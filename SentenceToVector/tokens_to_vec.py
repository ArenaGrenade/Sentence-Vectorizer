import numpy as np
from gensim.models import FastText


class WordToVector:
    mode_dict = {
        0: "50d",
        1: "100d",
        2: "200d",
        3: "300d"
    }

    def __init__(self, train_new_model=False, mode=0, tokenized_dataset=None, vector_size=100, train_epochs=30):
        self.word_weight_vec = None

        if not train_new_model:
            self.no_train = True
            with open("glove.6B." + self.mode_dict[mode] + ".txt", "rb") as model_file:
                self.word_vec_dict = {word_vec_pair.split()[0]: np.array(map(float, word_vec_pair.split()[1:]))
                                      for word_vec_pair in model_file}

        else:
            self.no_train = False
            if tokenized_dataset is not None:
                self.to_train_model = FastText(size=vector_size, window=4, min_count=2)
                self.to_train_model.build_vocab(sentences=tokenized_dataset)
                self.to_train_model.train(sentences=tokenized_dataset,
                                          total_examples=len(tokenized_dataset),
                                          epochs=train_epochs)
                self.word_vec_dict = dict(zip(self.to_train_model.wv.index2word, self.to_train_model.wv.syn0))
            else:
                print("You have not given a tokenized_dataset. Please ensure that it is in the format of list of list \
                of tokens and also that the parameter you have passed is not None")
        self.dim = len(next(iter(self.word_vec_dict)))

    def trainWithAdditionalData(self, tokenized_dataset_update):
        if not self.no_train:
            self.to_train_model.build_vocab(tokenized_dataset_update, update=True)
            self.to_train_model.train(tokenized_dataset_update,
                                      total_examples=len(tokenized_dataset_update),
                                      epochs=self.to_train_model.epochs)
            self.word_vec_dict = dict(zip(self.to_train_model.wv.index2word, self.to_train_model.wv.syn0))
            self.dim = len(next(iter(self.word_vec_dict)))

    def convertSentenceToVector(self, sentence):
        return np.array([
            np.mean([
                self.word_vec_dict[word] * self.word_weight_vec[word]
                for word in sentence if word in self.word_vec_dict]
                or [np.zeros(self.dim)], axis=0)
        ])
