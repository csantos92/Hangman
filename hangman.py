import random

#Movies

movie = ["THE MATRIX RELOADED", "THE TRUMAN SHOW", "FIGHT CLUB"]
movieBlank = ["___ ______ ________", "___ ______ ____", "_____ ____"]

#Random values

randomNumber = random.randint(0, 2)
randomMovie = movie[randomNumber]
randomBlank = [movieBlank[randomNumber],]

#Variables

gameOver, win = False, False
failedLetters, guessedLetters = 0, 0
failedList = []

#Functions

def showStats():
  print(hangman[failedLetters])
  print("            " + str(randomBlank[guessedLetters]) + "\n")
  print("Failed letters: " + ', '.join(failedList) + "\n")

def welcomeMessage():
  print("""

  ******** Welcome to the hangman game ******** 

          
  """)

def gameOverMessage():
  print("""

            The guy was killed!!!
            
                 GAME OVER
       """)

def gameWonMessage():
  print("""

            You saved the poor guy!
            
                  YOU WON
        """)

#Hangmans

hangman = ["""

                (*_*)
                  |
                / | \\
                  |
                /   \ 
     
    """,
    """

                (*_*)
                  |
                / | \\
                  |
                /   
       
    """,
    """

                (*_*)
                  |
                / | \\
                  |
                
  
    """,
    """

                (*_*)
                  |
                / | \\
                  
                
  
    """,
    """

                (*_*)
                  |
                / | 
                  
                
  
    """,
    """

                (*_*)
                  |
                  | 
                  
                
  
    """,
    """

                (*_*)
                  |
              
                

  
    """,
    """

                (*_*)
                  

                
  

    """]

#Welcome message

welcomeMessage()

#Game logic

while not(gameOver):
  
  showStats()
  
  letter = input("Enter a letter: ")

  while len(letter) != 1:
    letter = input("Enter a single letter: ")

  upperLetter = letter.upper()

  if upperLetter not in randomMovie:
    failedLetters += 1
    failedList.append(upperLetter)

    if failedLetters == 8:
        gameOver = True

  else:
    for i, ch in enumerate(randomMovie):

      if ch == upperLetter:

        lista = list(randomBlank[guessedLetters])
  
        for c in lista:
          print(lista[i])
          if lista[i] == "_":
            lista[i] = upperLetter
            guessedLetters += 1

        randomBlank.append("".join(lista))
            
    if guessedLetters == len(randomBlank[guessedLetters].replace(" ", "")):
      win = True
      break
          
#Prints Game Over message

if gameOver:
  gameOverMessage()

#Prints Game Won message

if win:
  gameWonMessage()