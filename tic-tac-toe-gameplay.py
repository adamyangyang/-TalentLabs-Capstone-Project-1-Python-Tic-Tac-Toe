#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
  position = int(position)
  
  pos_mark_input = {position: mark}
  
  if position in board.keys():
    board.update(pos_mark_input)

  return board


# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def printBoard():

  # Step 1: Get all keys & values from dictionary board
  
  # Create an empty list to capture both key & values of the board
  row_w_vals = []
  
  # For each key & value in the dictionary board
  for key, val in board.items():
  
    # If the value is empty
    if val == " ":
  
      # Replace the value with the key. If not empty, replace with player's marker.
      val = key
  
    # Put the values into the empty list
    row_w_vals.append(val)
  
  # Check output
  #print(row_w_vals)
  #print("")
  
  # Step 2: Separate numbers into 3's & create a nested list.
  
  # Create another empty list to separate all the values into equal size of 3 (ex: [1, 2, 3], [4, 5, 6], [7, 8, 9])
  chunk_list = []
  
  # For each element at the start of the Step 1's list (row_w_vals) to every 3rd, 6th & 9th position of row_w_vals
  for chunks in range(0, len(row_w_vals), 3):
  
    # Put the values into the new empty list (chunk_list)
    # Instead of appending 'chunks', we append the entire row_w_vals list
    # Then, we add the chunk element extracted into an inner list after row_w_vals
    # Followed by a ":" and a "+3" sign to indicate that we want the 1st element to the 3rd element from the chunk element extracted.
    chunk_list.append(row_w_vals[chunks:chunks+3])
  
  # Check output
  #print(chunk_list)
  #print("")
  
  # Step 3: Use a 3rd 'for loop' to print out each element from Step 2's list
  
  # For each list in the chunk list
  for c in chunk_list:
  
    # Print out the 1st, 2nd & 3rd element from each list
    print("", str(c[0]) + " |", str(c[1]) + " |", str(c[2]))
    
    # Print out separator
    print(" ---------")
    
  
  print("")
  



# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):
  
  # Intial check to ensure player doesn't enter empty string or a data type that's not INT.
  if position == "" or not str(position).isnumeric():
    print("\nPlease enter a number between 1 - 9.\n")
    return False

  # If passed, convert input into interger
  position = int(position)

  if position in board.keys():

    # Check if there's an empty space & match position to key.
    for p, v in board.items():
      if p == position and v == " ":

        # If successful, break out of loop & return True. 
        #print("\nYou marked position", str(position) + ".", "\n")
        print("\nPosition", p, "is marked.\n")
        break

      # If the position is already marked.
      elif p == position and v != " ":
        print("\nPosition", p, "is already occupied.\n")
        return False

  # If not within range
  else:
    print("\nNumber", position, "is outside the range. Please try a number between 1 - 9.\n")
    return False

  # Return True as final value from loop
  return True

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],

  # Vertical wins
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],

  # Diagonal wins
    [1, 5, 9],
    [3, 5, 7]

]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):

  # Create a empty list to capture all moves made by player
  moves_list = []
  for position, move in board.items():
    if move == player:
      moves_list.append(position)

  # If player wins in 3 moves, look for their winning combo in winCombinations.
  if len(moves_list) == 3 and moves_list in winCombinations:
    print("Player", player, "won!")
    return True

  # If player uses more than 3 moves to win
  elif len(moves_list) > 3:

    # Create a separate empty list to match the moves to winning combo.
    res = []
    
    # Start looping through each list in winCombinations
    for combos in winCombinations:
      for moves in moves_list:
        for nums in combos:

          # If there's a match, add the specified winning combo to the empty list
          if moves == nums:
            res.append(combos)

    # List comprehension for counting how many times each winning combo appeared
    # For each result in the empty list, create a 'counter' variable to count how many times that winning combo appeared
    count = [[res.count(r), r] for r in res]

    # Create another empty list to hold the winning combos & their total counts
    counter_and_combo_list = []

    # For each result in the count list (has int data type & list data type)
    for result in count:
      # If the counter vairable doesn't equal to 3, don't add to list & leave it empty (a.k.a no winning combinations was found).
      if result[0] != 3:
        pass
      # If the results equals to 3, add it to the counter & combo list & break out of loop.
      elif result[0] == 3:
        counter_and_combo_list.append(result)
        break

    # If the counter & combo list is empty, then no winning combo was found.
    if counter_and_combo_list == []:
      return False

    # Else, return what winning combo was found.
    else:
      win_combo_list = counter_and_combo_list[0][1]

      # Find the winning combo in the winCombinations list.
      if win_combo_list in winCombinations:
        print("Player", player, "won!")
        return True
        
  # If player doesn't win in 3 moves or more. return False.
  else:
    return False
  return False


# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():

  # If there's at least one empty space available, return false.
  if " " in board.values():
    #print("Board is not full.")
    return False
  # If all spaces are taken up, then return True.
  else:
    print("It's a tie!")
    return True 




#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
while not gameEnded:
  
    move = input(currentTurnPlayer + "'s turn, input: ")
    
    # 1: Validate if user input is valid
    if validateMove(move) == True:

      # 2: If valid, mark their position & print the updated board
      markBoard(move, currentTurnPlayer)
      printBoard()

      # 3: Check if a player has won the game or if it's a tie. 
      if (checkWin(currentTurnPlayer) or checkFull()) == True:

        # If true, change gameEnded status & ask if player wants to restart.
        gameEnded = True

        # Create a nested while loop to get player input
        while gameEnded == True:

          # Main message for asking if players want to restart.
          # Players can only choose Y (yes) or N (no)
          print("\nWould you like to play again?\n\nPlease enter Y / N\n")

          # Get player input
          restart_input = input()

          # Change player input to uppercase to match Y / N    
          restart_input = restart_input.upper()

          # If player wants to quit, show goodbye message.
          if restart_input == "N":
            print("\nAlright. Thanks for playing!")
            
            # Change gameEnded variable to break out of the 'gameEnded = True' while loop 
            gameEnded = "Ended"

          # If player enters an invalid input
          # Tell them they can only enter Y or N
          elif restart_input != ("Y" or "N"):
            print("\nSorry. You can only enter 'Y' or 'N'")

          # If player wants to restart the game
          else:
            print("\nOkay, let's restart the game.\n")
            
            # Change variable to False
            gameEnded = False

            # Create a new board to restart a game.
            newBoard = {
                        1: ' ', 2: ' ', 3: ' ',
                        4: ' ', 5: ' ', 6: ' ',
                        7: ' ', 8: ' ', 9: ' '
                       }

            # Update main board with values from newBoard 
            # as a way to 'restart' the game.
            board.update(newBoard)

            # Ensure 'X' always goes first
            currentTurnPlayer = "X"

            # Print message to indicate a new game has started.
            print("--------------------------")
            print("A new game has started!")
            print("--------------------------\n")
            
            # Call printBoard() function to show the new board
            printBoard()

            # Break out of loop
            break

        # If player chose to restart the game, break out of nested loop & restart main while loop from the start.  
        else:

          # Break out of while loop.
          break
        
      # 4: If no wins or tie, switch player & restart while loop.
      else:

        # If current player is 'X', switch to 'O'
        if currentTurnPlayer == "X":
          currentTurnPlayer = "O"
          
        # If current player is 'O', switch back to "X"
        else:
          currentTurnPlayer = "X"
          
      # Restart loop
      continue

    # If user input is invalid, restart while loop to get user input
    else:
      continue
          

# Bonus Point: Implement the feature for the user to restart the game after a tie or game over
