import setuptools

with open("README.md", "r") as help_file:
    long_description = help_file.read()

setuptools.setup(
    name="SentenceToVector", # Replace with your own username
    version="0.0.1",
    author="Rohan Asokan",
    author_email="rohan.asokan@students.iiit.ac.in",
    description="A package that converts sentences into a vector",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArenaGrenade/Sentence-Vectorizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)