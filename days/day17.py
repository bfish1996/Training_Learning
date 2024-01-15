from getpass import getpass as input
print("E P I C    🪨  📄 ✂️    B A T T L E")
print()
p1_counter = 0
p2_counter = 0
while True:
  player_1 = input("Player 1, select your move (R, P or S): ")
  player_2 = input("Player 2, select your move (R, P or S): ")
  if player_1 == "R":
    if player_2 == "R":
      print("It's a tie!")
    elif player_2 == "S":
      print("Player 1 wins!")
      p1_counter += 1
    elif player_2 == "P":
      print("Player 2 wins!")
      p2_counter += 1
    else:
      print("Invalid move Player 2!")
  elif player_1 == "P":
    if player_2 == "P":
      print("It's a tie!")
    elif player_2 == "S":
      print("Player 2 wins!")
      p2_counter += 1
    elif player_2 == "R":
      print("Player 1 wins!")
      p1_counter += 1
    else:
      print("Invalid move Player 2!")
  elif player_1 == "S":
    if player_2 == "S":  
      print("It's a tie!")
    elif player_2 == "R":
      print("Player 2 wins!")
      p2_counter += 1
    elif player_2 == "P":
      print("Player 1 wins!")
      p1_counter += 1
    else:
      print("Invalid move Player 2!")
  else: 
    print("Invalid move Player 1!")
  if p1_counter == 3 or p2_counter == 3:
    print ("The score is" , p1_counter, "to" , p2_counter)
    break
    exit()
  else:
    print("The score is" , p1_counter, "to" , p2_counter)
    continue