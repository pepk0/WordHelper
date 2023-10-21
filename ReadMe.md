# Wordy

Simple project, used to help with generating valid Bulgarian words  
from a specified sequence of letters and length.
I made program to  help me with solving word puzzles from a popular bulgarian mobile app.

### The App:
![app](https://i.imgur.com/6vNWu8F.jpg)  

> The mobile app has some random letters and the goal is to create a valid word.
> The problem is often you get stuck on a word and to get a hint, you need to sped money.  
----

#### Quick Demo:
![word_helper](https://i.imgur.com/YCFnT6z.gif)

### Usage:
---- 
 * In the dropdown menu chose the desired length of characters.
 * Enter the letter sequence in the input frame.
 * Click the Generate button to get the found words.

### Additional functionality
---- 
* __Cache functionality__
    >the cache functionality uses a python dictionary to cache previous queries, future quires in the dictionary instantly returned
* __Validate option__
    > this functionality validates the inputs, and sets the correct parameters if any are wrong
* __File not found error message__
    > Missing file or wrong file path, message is displayed if the file is missing or path is incorrect, instead of the program crashing
----

### How it works   
this program uses a txt file of bulgarian words, when a queries is made whit a sequence of elements and a specific length a permutation function is called and all permutations with the given length are created and stored in a list, a validate word function is called and we loop trough the list of validated words and check if any of them match the permutations

----
### Constrains
while the program uses a list of 270k validated bulgarian words, some if the mobile apps words may not appear in the words list.

