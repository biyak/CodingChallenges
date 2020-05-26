import csv 
import random

def characterGen():
  upbringing = ["orphan", "loving home", "single parent"]

  background = ["wealthy family", "humble beginnings", "middle class", "outsider", "streets", "streetrat", "theif"]

  chessPiece = ["king", "queen", "knight", "bishop", "rook", "pawn"]

  # hobbies = ["artist", "musician", "hunter", "gardening", "baking", "murdering", "reading", "vlogging", "poetry", "basketball", "coding", "video games", "activist"]

  ageRange = ["6 - 10", "11-15", "16-20", "16-20", "early twenties", "late twenties", "early thirties", "late thirties", "forty", "fifty", "sixty", "seventy", "eighty", "1000+", "no one really knows", "couple hundred", "prehistoric"]

  occupations = []

  gender = ["male", "female", "nonbinary", "other", "male", "female", "male", "female", "male", "female"]

  with open('occupations.csv') as occ:
      csv_reader = csv.reader(occ, delimiter=',')
      for row in csv_reader:
        occupations = occupations + row

  hobbies = open("hobbies.txt").readlines()

  # names = names + open("southasiannames.txt").readlines()


  print( "Upbringing: " + random.choice(upbringing) + "\n" + "Background: " + random.choice(background) +
  "\n" + "Chess Piece: " + random.choice(chessPiece) +
  "\n" + "Occupation: " + random.choice(occupations) +
  "\n" + "Age: " + random.choice(ageRange) +
  "\n" + "Hobbies: " + random.choice(hobbies) + 
  "\n" + random.choice(hobbies) +
  "\n" +random.choice(hobbies) +
  "\n" + "Gender: " + random.choice(gender) 
)


characterGen()

