import random

#Movies

movie = ["El señor de los anillos", "Yo Robot", "El padrino", "Piratas del caribe", "El hombre invisible", "Los siete samurai"]
movieBlank = ["__ _____ __ ___ _______", "__ _____", "__ _______", "_______ ___ ______", "__ ______ _________"
                , "___ _____ _______"]

#Random values

randomNumber = random.randint(0, 5)
randomMovie = movie[randomNumber]
randomBlank = [movieBlank[randomNumber],]

#Variables

gameOver, win = False, False
failedLetters, guessedLetters = 0, 0
failedList = []

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

print("""

******** Wellcome to the hangman game ******** 

          
""")

#Game logic

while not(gameOver):
    print(hangman[failedLetters])
    print("         " + str(randomBlank[guessedLetters]) + "\n")
    print("Failed letters: " + ', '.join(failedList) + "\n")

    letter = input("Enter a letter: ")

    if letter not in randomMovie:
        failedLetters += 1
        failedList.append(letter)

        if failedLetters == 8:
            gameOver = True

    else:
        for i, ch in enumerate(randomMovie):

            if ch == letter:

                lista = list(randomBlank[guessedLetters])
          
                for c in lista:
                    lista[i] = letter

                randomBlank.append("".join(lista))
                guessedLetters += 1

        if guessedLetters == len(randomBlank[guessedLetters].replace(" ", "")):
            win = True
            break
        
#Prints Game Over message

if gameOver:
        print("""

                The guy was killed!!!
                
                     GAME OVER
    """)

#Prints Game Won message

if win:
        print("""

                You saved the poor guy!
                
                       YOU WON
    """)