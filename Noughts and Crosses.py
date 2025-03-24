# Importing sys, datetime and os

import datetime
import sys
import os

# Creating a function to get the players names and define their playing symbols
def Player_Details():
    global Player1_Name, Player2_Name, Player1_Symbol, Player2_Symbol
    Symbols = ['X','O']                         # Define which symbols can choose
    Player1_Name = input("Enter your name : ")                                            # Get the name from the player1
    Player1_Symbol = input("Enter your prefer symbol from ('X' or 'O') : ").upper()         # Get the name from the player1
    while Player1_Symbol not in ['X','O']:
        Player1_Symbol = input("Invalid input.Please enter your prefer symbol from ('X' or 'O') only : ").upper()
        continue
        
    Symbols.remove(Player1_Symbol)                                          # Remove player1 chose symbol
    Player2_Symbol = Symbols[0]                                             # Give the other symbol to player2

    Player2_Name = input("\nEnter your name : ")                                    # Get the name from the player2

    print(f"\nPlayer1 is playing as {Player1_Name}, and playing with '{Player1_Symbol}' symbol." )                  # Printing player1 and player2 names and their symbols
    print(f"Player2 is playing as {Player2_Name}, and playing with '{Player2_Symbol}' symbol.\n" )
    print("============================================================")
    


# Creating a function to game menu to select option proceed,view result or exit the game
def game_menu():
    print("1 : Play a Game Round")
    print("2 : View the previous game results")
    print("3 : Exit from the Game\n")
    
    
    

# Creating a function to print the board to select a place to input position
def print_board(board):           
    for row in board:                       #Creating the row separators and column separators in the board
        print(" | ".join(row))              
        print("-" * 9)
        
    

# Creating a function to check if the current player won
def win_check(board,symbol):
    # Checking any player who win a row with same symbol 
    for row in board:                                                                                             
        if row[0] == symbol and row[1] == symbol and row[2] == symbol:
            return True
        
    # Checking any player who win a column with same symbol     
    for col in range(3):
        if board[0][col] == symbol and board[1][col] == symbol and board[2][col] == symbol:
            return True
        
    # Checking any player who win diagonals with same symbol     
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    
    # If the any player have no win from above conditions
    return False
  
          
# Creating a function to check if the game is a draw
def draw_check(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False            # If there has any empty cell , the is not drawn
    
    # All cells are filled now the game is draw        
    return True


# Creating a function to play the game
def Play_Game():
    # Initialize the empty 3x3 board 
    board = [[" " for i in range(3)] for i in range(3)]
    players = [Player1_Name , Player2_Name]                              # List of player
    symbols = [Player1_Symbol , Player2_Symbol]                          # List of symbols for the relevant players
    current_play_ind  = 0                               # Tracking the player index
    while True:
        print_board(board)                                          # Print the current board             
        print(f"{players[current_play_ind]}'s turn...\n")           # Printing to indicates which player has the turn 
        try:
            # Get the row number which the current player wanted
            row = int(input("Enter the row number(1-3) : ")) - 1 
            while not (row >= 0 and row < 3):           # Checking that row number is in the range 1 to 3
                
                # If that row number not in that range, re-enter the correct row number according to that 1 to 3 range 
                row = int(input("\nInvalid range.Please enter the row number from (1-3) : ")) - 1   
                continue
                
            else:
                # If that row number in the range, get the column number which the current player wanted
                col = int(input("Enter  the column number(1-3) : ")) - 1
                print()
                while not (col >= 0 and col < 3):           # Checking that row number is in the range 1 to 3
                    
                    # If that colum number not in that range, re-enter the correct column number according to that 1 to 3 range 
                    col = int(input("\nInvalid range.Please enter the column number from (1-3) : ")) - 1
                    print()
                    continue
                
                else:
                    if board[row][col] == " ":                  # If that row and column numbers in range, check that position is available or not
                        symbol = symbols[current_play_ind]      # Get the symbols of the current player place that into the board at the given position
                        board[row][col] = symbol                
                    
                    else:
                        print("\nThat is already taken.Try another one!!\n")          # Printing if that position is already taken
                        continue           
            
        except ValueError:
            print("\nInvalid input. Please enter number only..\n")             # Printing if the user's input isn't an integer
            continue
        
        
        # Checking for a which player is won
        if win_check(board,symbol):                 
            print_board(board)
            print(f"\n{players[current_play_ind]} wins!!\n")
            return f"\n{players[current_play_ind]} wins!!\n", board

        
        # Checking for a game is draw
        if draw_check(board):
            print_board(board)
            print("\nThe game is draw!!!\n")
            return "\nThe game is draw!!!\n", board
            
        # Switching to the next player's turn   
        current_play_ind = (current_play_ind + 1) % 2
    
        

# Creating a function to view the results of the previous game player after a game       
def View_Result():
    try:
        with open(f"History\\{filename}","r") as file:
            print("==================================================")
            print(file.read())                                           # Read and print the contents of the result file of the previous game
            print("==================================================")
            
    except FileNotFoundError:
        print("No game history found.\n")   # If there has not find any file game history
    
 
# Creating a function to view the results of all the previous games before playing game    
def First_View_Result():
    History_Folder = "History"                           # Define the folder name which the text files stored
    
    if not os.path.exists(History_Folder):               # If the folder not created yet or can not found
        print("No game history is found")
        return
    
    try:
        Files = os.listdir(History_Folder)               # List all the files which in that folder
        
        Filter_Files = []                                # Initialize a list 
        i = 1
        for File in Files:                               # Iterates every items in the folder
            
            if File.startswith("Session_Result_") and (File.endswith(".txt")):         # Devide the files starts with Session_Result_ and end with txt
                Filter_Files.append(File)                                              # Append that kind of files in to the list
                print(f"{i} : {File}")                                                 # Print the every files in that list
                i += 1
                
        if not Filter_Files:                                                        # Files not found
                print("No matching files found")
                return
            
        while True: 
            try:
                Option = int(input("\nEnter what number of file you want to view result : "))       # Get what file he wanted from above 
                if Option >= 1 and Option <= len(Filter_Files):
                    Selected_File = Filter_Files[Option - 1]
                    print(f"\nContent of the {Selected_File}\n\n")
                    with open(os.path.join(History_Folder, Selected_File), "r") as file:            # Read the file print the content
                        print("==================================================")
                        print(file.read())
                        print("==================================================")
                        break
                
                else:
                    print("\nInvalid option selected.\n")                                           # Enter the input in invalid range
                    continue
                   
            
            except ValueError:
                print("\nInvalid Input.Please enter valid number")        # If enter invalid input behalf an integer
                continue
            
    
    except:
        print("Invalid input for history!!!")            # Print invalid input for history

# Creating a function to create or existing text file and html file and write the content of the game session 
def Create_File(Player1_Tot, Player2_Tot, Draw_Tot):
    global filename,HTML_File                                   # Assign filename,HTML_File as a global variable
    Now_Time = datetime.datetime.now()                          # Get the current time using datetime module
    Play_Time = Now_Time.strftime("%Y/%m/%d_%H:%M:%S")          # Format the current time include for the content of the file
    File_Time = Now_Time.strftime("%Y%m%d_%H%M%S")
    filename = f"Session_Result_{File_Time}.txt"                         # Set the text filename for result text file
    HTML_File = f"Session_Result_{File_Time}.html"                         # Set the html filename for session html file
    
    if not os.path.exists("History"):
        os.makedirs("History")
    
    # Write the game statistics to the text file
    with open(f"History\\{filename}","w") as file:
        file.write("\n##################################################")
        file.write("\n\t    Noughts and Crosses\n")
        file.write("##################################################\n")
        file.write(f"\t    {Play_Time}")
        file.write("\n--------------------------------------------------")
        file.write(f"\nTotal Rounds Played : {Tot_Round}")
        file.write("\n--------------------------------------------------")
        file.write(f"\nTotal wins by Player 1 ({Player1_Name})\t  : {Player1_Tot}")
        file.write(f"\nTotal wins by Player 2 ({Player2_Name})\t  : {Player2_Tot}")
        file.write(f"\nTotal No. matches Drawn\t\t  : {Draw_Tot}\n")
        file.write("--------------------------------------------------\n")
    
    
    # Write the game statistics to the html file
    with open(f"History\\{HTML_File}","w") as htmlfile:
        htmlfile.write("<html>\n<head>\n<title><Noughts and Crosses</title>\n</head>\n<body>\n")
        htmlfile.write("<h1>Noughts and Crosses Game Results</h1>\n<br>\n")
        htmlfile.write(f"<label><b>Played Date & Time : {Play_Time}<br><br>Total Rounds Played : {Tot_Round}</b></label>\n<br><br>\n")
        htmlfile.write(f"<table border='1'>\n<tr>\n<th>Player 1 ({Player1_Name}) Wins</th>\n<th>Player 2 ({Player2_Name}) Wins</th>\n<th>Draws</th>\n</tr>\n")
        htmlfile.write(f"<tr>\n<td>{Player1_Tot}</td>\n<td>{Player2_Tot}</td>\n<td>{Draw_Tot}</td>\n</tr>\n")
        htmlfile.write("</table>\n")
        htmlfile.write("</body>\n</html>")
        
        
    print(f"\nSession stats saved to {filename} and {HTML_File}\n")
    
    


# Initialize the global variables for the game
Result = 0
game_choice = 0
board = []
Now_Time = 0
Format_Time = 0
File_Time = 0
filename = 0
Player1_Tot = 0
Player2_Tot = 0
Draw_Tot = 0
Choice = 0
Tot_Round = 0
Option = 0
Player1_Name = 0
Player2_Name = 0
Player1_Symbol = 0
Player2_Symbol = 0


# Welcome message for the game
print("-"*60)
print("\tWelcome to the game 'Noughts and Crosses... ")
print("-"*60)

Player_Details()


# Main game loop
while True:
    try:
        game_menu()
        game_choice = int(input("Enter the choice from the Game Menu : "))
        print()
        
        if game_choice == 1:                # Starting the playing round
            print("Starting a new round...\n")
            
            
            
            while True:
                
                # Calculate Player1 Wins, Player2 Wins, Total of drawn matches, Total matches round
                Result,board = Play_Game()
                if Player1_Name in Result:
                    Player1_Tot += 1
                elif Player2_Name in Result:
                    Player2_Tot += 1
                else:
                    Draw_Tot += 1
                
                Tot_Round += 1
                
                
                # Asking the user for continue or exit from the game
                Choice = input("Do you want to play another game (y/n) : ").lower()  
                print()     
                while Choice not in ['y','n']:
                    Choice = input("Invalid input.Please use 'y' for yes or 'n' to no : ").lower()
                    print()
                    continue
                
                # If the user don't want to play another session
                if Choice == 'n':
                    Create_File(Player1_Tot,Player2_Tot,Draw_Tot)
                    break
                
                
                
        elif game_choice == 2:                  # User to view the previous game result
            if Tot_Round >= 1:
                print("Viewing the previous game results...\n")
                View_Result()
                
            else:
                First_View_Result()
                print()
            
        
        elif game_choice == 3:                  # User exit from the game
            if Tot_Round >= 1:                  # Checking the user played at least one game
                print("Exiting the game. GoodBye!!!..\n")
                sys.exit(1)                     # If the player played at least one game exit the game
            else:
                print("You can not exit play at least one game\n")
                continue                        # If the player didn't playing at least a single game continue the session
        
        else:
            print("Invalid choice. Please choose a valid option from the menu...\n")
            continue
        
    except ValueError:
        print("\nInvalid input option, Please enter correct input!!\n")
        continue
        