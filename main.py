#****************************************************************
#Name:GOODNEWS AGBADU

#
#ANA1001 Assignment 9
#****************************************************************

'''Open a blank file and write a few lines about what you have learned in the course. Save the file as python_learning.txt In the same folder, write a program that reads what you wrote and prints it to the terminal three times .'''

#assigning filename to the file python_learning.txt
filename = "python_learning.txt"
#Opening the file in read mood
with open (filename, "r") as foj:
  '''reading the file line by line'''
  file = foj.readlines()
#using a for loop to print it out three times
for n in range (0,3):
  for line in file:
#printing out without space
    print(line.rstrip())
  print("\n")



'''Write a program that asks a user for their age, store this data in a file called age.txt and loop the input in a while loop so that only valid responses are stored. If the response is valid, store the age and let the user know their age in dog years (age multiplied by 7)(do not store that information). If the input is invalid (for example, the user types in five) loop the input again and ask them to try again.'''

#Write a program that asks a user for their age
while True:#using a while loop so that only valid responses are stored
  
  filename = 'age.txt'#creating a file to store the data
  #using a try/except/else chain 
  try:
    human_age = int(input("How old are you? "))
#opening filename with append mode
    with open(filename, "a") as file_object:
      file_object.write(str({human_age}))
#function to let code run when value error happens      
  except ValueError:
    pass
  else:
    d_age = human_age *7
    print("Your age in dog's years is", d_age)
    break
    

'''Write a program that tries to read a file that is not there and have it pass silently (no error message is displayed)'''
#writing file that is not there
filenames = ['me.txt', 'adi.txt']

#using a for loop on file
for filename in filenames:
#using a try/except/else chain    
  try:
    with open(filename) as file_object:
      contents = file_object.read()

  except FileNotFoundError:
    pass

  else:
    print(f"\nReading file: {filename}")
    print(contents)
    


'''Download a book from Project Gutenberg in text format.  https://www.gutenberg.org/ebooks/ read these files into a program and analyze the text to find out how many times the word “the” appears. Remember to check both cases “The and the” by converting the words you are looping are using .lower() This will also count words like then and there, so also count the number of times “the “ appears and print out both numbers and the difference between them. Then, using https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/ or another resource, find out the most common words in your book. Include your book file in your submission, it should be in the same folder as the code in your zip file.'''

#assigning filename to TheManFromtheClouds.txt
filename = "TheManFromtheClouds.txt"

def count_common_words(filename, word):
    """Count how many times word appears in the text."""
#using a try/except/else chain    
    try:
      with open(filename, encoding='utf-8') as foj:
          contents = foj.read()
    except FileNotFoundError:
      pass
    else:
      word_count = contents.lower().count(word)
#assignig msg with f string and print out message 
      msg = f"'{word}' appears in {filename} about {word_count} times."
      print(msg)

#printing out the number of time 'the' and 'the ' appeard in TheManFromtheClouds.txt
count_common_words(filename, 'the')
count_common_words(filename, 'the ')

#importing collections
import collections
import re #regular expression matching operations

#Finding the most common words using regular expression matching operations
words = re.findall(r'\w+', open("TheManFromtheClouds.txt").read().lower())
#Using the collection model the counter function 
most_common = collections.Counter(words).most_common(1)
#Printing most common word
print(f" The most common word to appear in The Man From the Clouds is {most_common}")

#Reference 
#https://www.youtube.com/watch?v=Pcyuaj5lCtA