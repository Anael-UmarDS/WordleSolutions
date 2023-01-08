#Open File Dictionary.txt

han = open('Dictionary.txt')

#Read all the lines in the file

Lines = han.readlines()

#Close File Handle

han.close()

# Create Validate function to check if the input is a single alphabet letter
# It return the letter in lowercase if it validates or print sorry and break the loop
# If input is none then it returns None
# The procedure will have a parameter called LETTER

def validate_input(LETTER):
      while True:
        if len(LETTER) == 0:
          return None
        if len(LETTER) == 1 and LETTER.isalpha():
          return LETTER.lower()
        else:
          print('Sorry, please enter a single alphabetic letter')
          break
          
#Create validate function for number of unknown characters (num_char)
#This function checks of num_char is a number and is not greater than 5
#This will use a parameter called NUMBER

def validate_num_char(NUMBER):
  NUMBER = int(float(NUMBER))
  if NUMBER <= 5:
    return NUMBER
  else:
    print('Sorry, please enter a number less than 5') 
    return 100 
    
    
    
def validate_elim_char(NUMBER):
  NUMBER = int(float(NUMBER))
  if NUMBER:
    return NUMBER
  else:
    print('Sorry, please enter a number less than 5') 
    return 100
    

#Objective 1: Ask for inputs and validate for 5 characters
print('This is the Wordle Solutions. Enter KNOWN characters in specific positions and I will find the solution for you!')

first_char = input('Enter first character or press Enter: ')
first_char = validate_input(first_char) # Validate input

second_char = input('Enter second character or press Enter: ')
second_char = validate_input(second_char) # Validate input

third_char = input('Enter third character or press Enter: ')
third_char = validate_input(third_char) # Validate input

fourth_char = input('Enter fourth character or press Enter: ')
fourth_char = validate_input(fourth_char) # Validate input

fifth_char = input('Enter fifth character or press Enter: ')
fifth_char = validate_input(fifth_char) # Validate input





#Users can also provide or not provide characters that may be in any position in the 5 letter word

num_char = input('How many characters are in UNKNOWN places? ')

#Create any_char list and set it to empty list to allow unknown positioned characters to be stored for use later
any_char = [] 

#Check if the given character is not empty, then continue
#Validate num_char and check if it is a number and is less than or equal to 5
#Loop for number of unknown characters, num_char and append the user input into any_char list
if num_char != '':
  num_char = validate_num_char(num_char)
  if num_char <= 5:
    for i in range(1,num_char + 1):
      unknown_char = input('Enter the unknown character: ')
      unknown_char = validate_input(unknown_char)
      any_char.append(unknown_char) 
      i = i + 1
      
      
      
#Users can also provide or not provide characters that do not have to be included in the word
elim_char = input('How many characters do you want to EXCLUDE? ')

#Create del_char list and set it to empty list to allow deleted characters to be stored for deletion later
del_char = []

#Check if the given character is not empty, then continue
#Validate elim_char and check if it is a number and is less than or equal to 5
#Loop for number of eliminating characters, elim_char and append the user input into del_char list
if elim_char != '':
  elim_char = validate_elim_char(elim_char)
  for i in range(1,elim_char + 1):
    grey_char = input('Enter the excluded character: ')
    grey_char = validate_input(grey_char)
    del_char.append(grey_char) 
    i = i + 1


# Create a string for evaluation conditional later in program
# The following will check if the characters are having a value. The cond variables will be used to show that the character is having value.
str1 = ''
cond_1 = 0
cond_2 = 0
cond_3 = 0
cond_4 = 0
cond_5 = 0

# This string will be passed into evaluation using the eval function later on after going through the events below
# If the character given has value and is not NoneValue, then the condition variable corresponding for that character will be 1

if first_char is not None:
  str1 = str1 + 'line[0] ==' + '"' + first_char.lower() + '" ' # Add the following to the string
  cond_1 = cond_1 + 1

if second_char is not None:
  if cond_1 == 1:
    str1 = str1 + 'and '
  str1 = str1 + 'line[1] ==' + '"' + second_char.lower() + '" ' # Add the following to the string...If cond_1 is 1, then there will be an 'and'
  cond_2 = cond_2 + 1

if third_char is not None:
  if (cond_1 == 1 or cond_2 ==1):
    str1 = str1 + 'and '
  str1 = str1 + 'line[2] ==' + '"' + third_char.lower() + '" ' # Add the following to the string...If the either one of the conditions before are true, then it will add an 'and' to the string statement
  cond_3 = cond_3 + 1

if fourth_char is not None:
  if (cond_1 == 1 or cond_2 ==1 or cond_3 == 1):
    str1 = str1 + 'and '
  str1 = str1 + 'line[3] ==' + '"' + fourth_char.lower() + '" ' # Add the following to the string...If the either one of the conditions before are true, then it will add an 'and' to the string statement
  cond_4 = cond_4 + 1

if fifth_char is not None:
  if (cond_1 == 1 or cond_2 ==1 or cond_3 == 1 or cond_4 == 1): # Add the following to the string...If the either one of the conditions before are true, then it will add an 'and' to the string statement
    str1 = str1 + 'and '
  str1 = str1 + 'line[4] ==' + '"' + fifth_char.lower() + '" '


#Set i to 0 for the loop
i = 0
#Check if the user has input unknown chars and any_char list is not empty, then add the conditional string logic in the previous string
if bool(any_char):
  if (cond_1 == 1 or cond_2 == 1 or cond_3 == 1 or cond_4 == 1 or cond_5 == 1):
    str1 = str1 + 'and '
  for letter in any_char:
    str1 = str1 + '(line[0]==' + '"' + letter + '" or '
    str1 = str1 + 'line[1]==' + '"' + letter + '" or '
    str1 = str1 + 'line[2]==' + '"' + letter + '" or '
    str1 = str1 + 'line[3]==' + '"' + letter + '" or '
    str1 = str1 + 'line[4]==' + '"' + letter + '") '
    if i < num_char - 1:
      str1 = str1 + ' and '
    i = i + 1
    
    
#Set i to 0 for the loop
i = 0

#Check if the user has input characters that need to be deleted and del_char list is not empty, then add the conditional string logic in the previous string
if bool(del_char):
  if (len(str1) >2 ):
    str1 = str1 + 'and not ( '
  for letter in del_char:
    str1 = str1 + '(line[0]==' + '"' + letter + '" or '
    str1 = str1 + 'line[1]==' + '"' + letter + '" or '
    str1 = str1 + 'line[2]==' + '"' + letter + '" or '
    str1 = str1 + 'line[3]==' + '"' + letter + '" or '
    str1 = str1 + 'line[4]==' + '"' + letter + '") '
    if i < elim_char - 1:
      str1 = str1 + ' or '
    i = i + 1
  str1 = str1 + ' ) '
  
#Create a blank solution list and evaluate the created string logic
Solutions = []
#Go through the Lines and see if the length is 6(0,1,2,3,4,5), then it will evaluate the string to search for the words that could fit the solution
for line in Lines:
    if len(line) == 6:
      if eval(str1): #Evaluate the string statement in an if condition
        Solutions.append(line.strip())
        #Append or add the line to the list of solutions

if len(Solutions) > 100: #If the total number of solutions amounts to being greater than 100, then print an error statement.
  print('Sorry, too much data, please enter more characters for more specific answer')
elif Solutions == []: #If the list remains empty, then print a sorry statement saying that there were no matches
  print('Sorry, there are no words to be found that relate to your search. Please try again')
else: # Print the answers
  print(len(Solutions), 'solutions meet your criteria: ', Solutions)

