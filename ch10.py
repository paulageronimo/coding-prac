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