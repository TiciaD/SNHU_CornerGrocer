import re
import string

# count all items and number of occurrences
def count_all_items():
  # initialize dictionary to hold item and item count key-value pairs
  all_items = dict()

  # Open file in read mode
  text = open("grocery.txt", "r")
  # loop over every line in file
  for line in text:
    # remove extra white space on each line
    word = line.strip()
    
    # if word is already in dictionary
    if word in all_items:
      # increment number of times word appears
      all_items[word] = all_items[word] + 1
    else:
      # if the word is not in dictionary, add it with a value of 1
      all_items[word] = 1
  
  # Close the opened file
  text.close()
  # return the dictionary
  return all_items


# print to console all items and number of ocurrences
def print_all_items():
  # call count_all_items function and assign returned dictionary to all_items
  all_items = count_all_items()

  # loop over dictionary passed as argument
  for key, value in all_items.items():
    # Print all contents of the dictionary
    print(key, ":", value)
  

# counts number of occurrences of search term passed.
def count_all_ocurrences(searchedItem):
  # convert search term to lowercase
  searchedItem = searchedItem.lower()
  # initialize count
  count = 0

  # Open file in read mode
  text = open("grocery.txt", "r")

  # loop over every line in file
  for line in text:
    # remove extra white space on each line and convert to lowercase
    word = line.strip().lower()
    
    # if word matches the search term
    if word == searchedItem:
      # increment count
      count += 1
      
  # Close the opened file
  text.close()
  print(f'{searchedItem} was purchased {count} times')
  # return final count
  return count


# creates new document with count of all items and number of occurrences
def write_frequency_data():
  # Open file in Write mode
  frequency = open("frequency.dat", "w")

  # call count_all_items function and assign returned dictionary to all_items
  all_items = count_all_items()

  # loop
  for key, value in all_items.items():
    frequency.write(str(key) + " " + str(value) + "\n")

  # Close the opened file
  frequency.close()
