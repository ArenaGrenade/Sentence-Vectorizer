from distutils.core import setup

setup(
    name="SentenceToVector", # Replace with your own username
    packages=["SentenceToVector"],
    version="0.0.1",
    license="MIT",
    author="Rohan Asokan",
    author_email="rohan.asokan@students.iiit.ac.in",
    description="A package that converts sentences into a vector",
    long_description_content_type="text/markdown",
    url="https://github.com/ArenaGrenade/Sentence-Vectorizer",
    download_url="https://github.com/ArenaGrenade/Sentence-Vectorizer/archive/v1.2.tar.gz",
    install_requires=[
        "nltk",
        "numpy",
        "gensim"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)