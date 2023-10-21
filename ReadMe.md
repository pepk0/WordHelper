# Wordy

Simple project, used to help with generating valid Bulgarian words  
from a specified sequence of letters and length.
I made a program to  help me with solving word puzzles from a popular Bulgarian mobile app.

### The App:
![app](https://i.imgur.com/6vNWu8F.jpg)  

> The mobile app has some random letters and the goal is to create a valid word.
> The problem is often you get stuck on a word and to get a hint, you need to spend money.  
----

#### Quick Demo:
![word_helper](https://i.imgur.com/YCFnT6z.gif)

### Usage:
---- 
 * In the dropdown menu choose the desired length of characters.
 * Enter the letter sequence in the input frame.
 * Click the Generate button to get the found words.

### Additional functionality
---- 
* __Cache functionality__
    > The cache functionality uses a Python dictionary to cache previous queries, future quires in the dictionary are instantly returned
* __Validate option__
    > This functionality validates the inputs and sets the correct parameters if any are wrong
* __File not found error message__
    > Missing file or wrong file path, A message is displayed if the file is missing or the path is incorrect, instead of the program crashing
----

### How it works   
this program uses a Txt file of Bulgarian words, when a query is made with a sequence of elements and a specific length a permutation function is called and all permutations with the given length are created and stored in a list, a validate word function is called and we loop through the list of validated words and check if any of them match the permutations

----
### Constraints
while the program uses a list of 230k+ validated Bulgarian words, some of the mobile app's words may not appear in the words list.

