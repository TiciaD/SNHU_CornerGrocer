# Corner Grocer Item-Tracking Program

## Functionality
Address the following:
1. Produce a list of all items purchased in a given day along with the number of times each item was purchased.
2. Produce a number representing how many times a specific item was purchased in a given day.
3. Produce a text-based histogram listing all items purchased in a given day, along with a representation of the number of times each item was purchased.

***

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

ENDFUNCTION

```

## Part 2
Use C++ and Python to produce a list of all items purchased in a given day along with the number of times each item was purchased

### Variables
### Functions