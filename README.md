# WordleSolutions

Objective
The program, Wordle Solution, is inspired by Wordle created by The New York Times. In Wordle, the main goal is to guess a word in 6 tries. This can be hard for some users which is why this program is created.
The program helps users by giving a list of possible solutions from Dictionary.txt for the Wordle from user inputs.
1. Users provide characters that are in **known positions** in a 5 letter word
2. Users can also provide or not provide characters that may be in **any position** in the 5 letter word
3. Users can also provide or not provide characters that needs to be **excluded** from the word

Procedures and Lists
Procedures:

There are 3 procedures involved in this program.
1. validate_input()
2. validate_num_char()
3. validate_elim_char()

All 3 of these procedures are to validate a certain character or number given by the user. The first procedure checks to see if the user input is a single alphabet. The second function checks to see if the user input for num_char, a variable that asks the user for the number of characters in unknown placement, is a number less than 5. The last procedure validates elim_char, a variable that asks the user how many characters need to be excluded from the word. It makes sure that the input is a number.

Lists:

There are 3 lists involved in the program.
1. any_char
2. del_char
3. Solutions

The first list, any_char, is a list that contains all the unknown characters that the user inputted. This lists is later used in a conditional. The length of this list will be the same as num_char. The second list, del_char, is a list of characters that the users wants to delete or exclude from the word. This is also used in the same conditional as any_char. The length of this list is the same as elim_char. The last list is Solutions. This list will print out all solutions that fit the user inputs. This list is very helpful as it organizes all the information in a suitable fashion.


Description
* The program will ask users for known characters
* These known characters are in specific positions
* The program will also ask users if they have characters that are in unknown positions
* The program will also ask users if they characters they do not want to include
* These characters will later be used to create a string that would be incorporated into a conditional
* Using these characters, the program opens a CSV file called Dictionary.txt and searches for words that contain the characters
* The program asks users for inputs
* Using a procedure called validate_input, the program will verify that the entered characters are single alphabetic letters
* Program also allows user to input a number of characters in any position and ask how many characters the user wants to input as num_char. The procedure called validate num_char will verify that the inputs are integers
* A logical string statement is created based on the input which is evaluated using the eval function later on in the program
* A list called any_char is created, which contains all inputs from num_char in a list
* The program looks in the dicitonary and checks if the length is 6 and the characters are in words contained by the dictionary
* We then create a list called "Solutions"
* If the words in the dictionary contain the letters, they will be added to Solutions and it will be printed as possible solutions
* Additionally, if the length of Solutions exceeds more than 100, then the program will ask the user to enter more characters
