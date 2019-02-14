# -*- encoding:utf-8 -*-

def hangman(step):
  # Top
  print("  ________")
  print("  | /     |")
  # Head
  if step >= 5:
    print("  |/      0")
  else:
    print("  |/")
  # Arms and torso
  if step >= 8:
    print("  |      /|\\")
  elif step >= 7:
    print("  |      /|")
  elif step >= 6:
    print("  |       |")
  else:
    print("  |")
  # Torso
  if step >= 6:
    print("  |       |")
  else:
    print("  |")
  # Legs
  if step >= 10:
    print("  |      / \\")
  elif step >= 9:
    print("  |      /")
  else:
    print("  |")
  # Bottom / Stool
  if step >= 4:
    print("  |       ^")
  else:
    print("  |)")
  if step >= 3:
    print(" /|\\     /|\\")
  elif step >= 2:
    print(" /|\\     / \\")
  elif step >= 1:
    print(" /|\\     /")
  else:
    print(" /|\\")


if __name__ == "__main__":
  for i in range(11):
    print("Level %i:" % i)
    hangman(i)
    print("")
