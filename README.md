# Sentence-Vectorizer
A simple package that given a list of sentences converts each of them to a vector. It is essentially a wrapper around other NLP libraries.

This package can be used for the following purposes:

1. Convert any given sentence into a `bag of words` using operations from nltk python library.
2. Using a TF-IDF conversion method, conversion of a bag of words to a vector

Using the vector from the TF-IDF, one can easily plug into any NN as they work on vectors.

## Simple usage with a given tokenized dataset
You will have to import the following:
```python
import SentenceToVector
```
Here we use data to be the tokenized dataset:
```python
data= [
    ['computer', 'aided', 'design'],
    ['computer', 'science'],
    ['computational', 'complexity'],
    ['military', 'supercomputer'],
    ['central', 'processing', 'unit'],
    ['onboard', 'car', 'computer']
]
```
Now, create a WordToVector object that is part of the SentenceToVector library:
```python
s2v= SentenceToVector.WordToVector(train_new_model=True, tokenized_dataset=data, vector_size=20)
```
Here we have kept the vector_size to 20 for faster training times.

Now, we add a __main__ segment that runs the trainer and gives us an example output:
```python
if __name__ == '__main__':
    word = input("Enter any word: ")
    print(s2v.getWordVector(word))
```
Here, we can enter any word that is not even in the dataset and the code will still generate a vector corresponding to it.


# TODO

Have to update the order of imports to remove a massive breaking bug in the package hosted on pypi.
Need to add other methods of vectorization as well.

