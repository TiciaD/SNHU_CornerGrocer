# Corner Grocer Item-Tracking Program

## Functionality

Address the following:

1. Produce a list of all items purchased in a given day along with the number of times each item was purchased.
2. Produce a number representing how many times a specific item was purchased in a given day.
3. Produce a text-based histogram listing all items purchased in a given day, along with a representation of the number of times each item was purchased.

## Part 1

Use C++ to develop a menu display that asks users what they would like to do including options for each of the three requirements.

### Variables

`userInput` ---> INPUT user input

### Functions

`displayMenu()` ---> DISPLAY options to console  
`readNumber()` ---> READ user input and validate it as an integer

### Pseudocode

```
FUNCTION displayMenu

  DISPLAY 1. all items purchased and number of times each was purchased
  DISPLAY 2. number of times a specific item was purchased
  DISPLAY 3. generate histogram of all items purchased and number of times each was purchased
  DISPLAY 4. Quit

ENDFUNCTION


FUNCTION readNumber(prompt)

  DISPLAY prompt
  VAR userInput = INPUT

  WHILE true
    IF input fails
      clear stream
      DISPLAY error message
      userInput = INPUT
    ELSE
      break
    ENDIF
  ENDWHILE

  RETURN userInput

ENDFUNCTION

```

## Part 2

Use C++ and Python to produce a list of all items purchased in a given day along with the number of times each item was purchased

### Variables

`allItems` ---> list of all unique items and number of occurrences  
`word` ---> string value of a word from the text file

### Functions

`getAllItems()` ---> returns list of all unique items and occurrences and prints them to the console

### Pseudocode

```
FUNCTION getAllItems

  ItemsFile = openRe­ad(­"­GroceryItems.tx­t")
  DICTIONARY allItems
  VAR word

  FOR line in ItemsFile
      word = myFile.re­adL­ine()
    IF word IN allItems
      allItems[word] = allItems[word] + 1
    ELSE
      allItems[word] = 1
    ENDIF

  ItemsFile.cl­ose()

  FOR key in allItems
    PRINT key : allItems[key]

ENDFUNCTION
```

## Part 3

Use C++ and Python to return a number representing how many times a specific item was purchased

### Variables

`numPurchases` ---> tracks count of item ocurrence

### Functions

`getNumOfPurchases(item)` ---> gets passed item to search for and tallies how many times that item is found in text file, returns that tally

### Pseudocode

```
FUNCTION getNumOfPurchases (item as STRING)

  ItemsFile = openRe­ad(­"­GroceryItems.tx­t")
  VAR count

  FOR line in ItemsFile
      word = myFile.re­adL­ine()
      IF word == item
        count =  count + 1
      ENDIF

  ItemsFile.cl­ose()

  RETURN count

  ENDFUNCTION
```

## Part 4

Use C++ and Python to produce a text-based histogram listing all items purchased and number of times each item was purchased

### Variables

`allItems` ---> list of all unique items and number of occurrences  
`word` ---> string value of a word from the text file

### Functions

`writeFrequencyFile()` ---> creates a dat file and writes all unique items and number of occurrences read from grocery file to it  
`createHistogram()` ---> reads dat file and creates histogram based off of all items purchased and number of times each item was purchased

### Pseudocode

```
FUNCTION writeFrequencyFile

  FrequencyFile = openWrite(­"­frequency.dat")

  ItemsFile = openRe­ad(­"­GroceryItems.tx­t")
  DICTIONARY allItems
  VAR word

  FOR line in ItemsFile
    word = myFile.re­adL­ine()
    IF word IN allItems
      allItems[word] = allItems[word] + 1
    ELSE
      allItems[word] = 1
    ENDIF

  ItemsFile.cl­ose()

  FOR key in allItems
    write key allItems[key]

  FrequencyFile.close()

ENDFUNCTION

FUNCTION createHistogram()

    FrequencyFile = openRe­ad(­"­­frequency.dat")

    itemName = FrequencyFile.readLine()
    itemQuantity = FrequencyFile.readLine()

    while NOT FrequencyFile.en­dOf­File()
      FOR i = 0 to itemQuantity
        PRINT '*'

      itemName = FrequencyFile.readLine()
      itemQuantity = FrequencyFile.readLine()
    ENDWHILE

    FrequencyFile.close()

ENDFUNCTION
```
