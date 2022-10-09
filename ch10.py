import random

def hangman(word):
  wrong = 0
  stages = ["",
            "________        ",
            "|               ",
            "|        |      ",
            "|        0      ",
            "|       /|\     ",
            "|       / \     ",
            "|               "
            ]
  rletters = list(word)
  board = ["__"] * len(word)
  win = False
  
  print("Welcome to Hangman")
  guesses = []
  while wrong < len(stages) - 1:
    print("\n")
    
    char = input("Guess a letter: ")
    while char in guesses:
      print("You already input that letter! Try another one.")
      char = input("Guess a letter: ")
    
    guesses.append(char)
    
    if char in rletters:
      cind = rletters.index(char)
      board[cind] = char
      rletters[cind] = '$'
    else:
      wrong += 1
    
    print((" ".join(board)))
    e = wrong + 1
    print("\n".join(stages[0: e]))
    
    if "__" not in board:
      print("You win!")
      print(" ".join(board))
      win = True
      break
    
  if not win:
    print("\n".join(stages[0: wrong]))
    print("You lose! It was {}.".format(word))

if __name__ == '__main__':
  # random lists of words I decided to come up with.
  words= {  "easy": ["cat", "run", "car", "tea", "red", "pot"],
            "medium": ["mouse", "apple", "tree", "doubt"],
            "hard": ["johnson", "mediocre", "monopoly", "juxtaposition", "xylophone"]}
  
  level = input("Input difficulty.\nOptions:\n - easy\n - medium \n - hard\n")
  
  # continues game even if input is not in list
  # by generating random difficulty
  if level not in words:
    level = list(words)[random.randrange(3)]
  
  # gets length of the list, since they're all different sizes
  # this reduces the need to hard code numbers.
  lenSubList = len(words[level])
  
  # gets the words list from the respective level 
  # then generates the random index of the hangman word.
  word = words[level][random.randrange(lenSubList)]
  
  hangman(word)