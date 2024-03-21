# Word Helper

A program made to help with finding valid Bulgarian words.
I enjoy crosswords, but sometimes I cant find (or don't even know) a valid
word, to make my life easier, instead of going online or looking in a dictionary
I automated the looking with Python.

### Quick Demo:

![word_helper](https://i.imgur.com/YCFnT6z.gif)

### The Problem that inspired me:

> In the below examples I have used a popular word puzzle app in Bulgaria that I
> play.  
> The mobile app has some random letters and the goal is to create a valid
> word.  
> Problem is often you get stuck on a word and to get a hint, you need to spend
> money.

![app](https://i.imgur.com/6vNWu8F.jpg)


----

## How to run:

You can clone this repository and run the main.py file.  
First you need to be in the cloned repository and then you can run:

  ~~~ powershell
  py main.py
  ~~~

Creating a virtual environment is recommended, you can create like this

  ~~~ powershell
  py -m venv venv
  ~~~

### Usage:

1. In the dropdown menu choose the desired length of the output words.
2. Enter the letter sequence in the text input bar.
3. Click the Generate button.

| **Program output**                                         | **Crossword**                                 |
|------------------------------------------------------------|-----------------------------------------------|
| ![program with 3 letters](https://i.imgur.com/mUDbM0z.jpg) | ![crossword](https://i.imgur.com/GkPUtC2.jpg) |
| ![program with 4 letters](https://i.imgur.com/0be41fJ.jpg) | ![crossword](https://i.imgur.com/2muhuM2.jpg) |
| ![program with 5 letter](https://i.imgur.com/jl0cpTs.jpg)  | ![crossword](https://i.imgur.com/1cRONjM.jpg) |

---- 

## Additional functionality:

###    * __Cache functionality__

The cache functionality uses a Python dictionary to cache previous queries,
future quires that are stored in the dictionary are instantly returned.

###    * __Validation__

This functionality validates the inputs displays the appropriate error message
if any are wrong.

###    * __File Manager__

The file manager system manages the txt files containing all the words.

* A script called length_splitter splits the words from the base txt
  file in to length specific files containing only words with equal lengths,
  this limits the search only to words with the same length as the desired one.
  All the separate length files are present by default.  
  To run the script use:
  ~~~ powershell
  py .\valid_words\lenght_splitter.py
  ~~~

----

## How it works:

This program uses a txt file of bulgarian words, when a query is made with a
sequence of elements and a specific length, a permutation function is called and
all permutations with the given length are created and stored in a list, a
validate word function is called and a loop runs through the list of validated
words, and checks if any of them match the permutations.

----

## Constraints:

While the program uses a list of 230k+ validated Bulgarian words, some of the
mobile app's words may not appear in the words list.

----
