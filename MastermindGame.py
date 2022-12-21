'''
Andrew Habib
8 October 2021
Mastermind Program
'''

# From the tkinter library import the following modules to aid in creating a Graphical User Interface
# These modules enable one to create objects that may be used to formulate enhanced and essential features to create a functioning interface
from tkinter import Tk, Frame, PhotoImage, Label, Button, Message, messagebox

# Import a module that adds more options for creating randomizing objects not included in python
import random

# Define a function that is responsible for handling events when the game is first started (The start button is clicked)
# These will set the starting points for the game and initialize all essential game components to start a fresh new game interface
def commence_game():

    # Declare the following variables and lists as global variables and lists 
    # These variables and lists may now be accessed and manipulated within the current function
    global attempts, rng_colourSequence, generatedColourPattern, list2DGameButtons

    # Set the attempts variable storing the current attempt number of the user to one
    # Indicates that user is just starting the game and this is their first attempt
    attempts = 1

    # Update and configure the start button by changing its state to disabled as the user has already started the game and there is no more purpose for this button
    btnStart.config(state='disabled')

    # Update and configure the submit button by changing its state to normal as the user will need to submit their colour guess every round to be checked with each attempt
    btnSubmit.config(state='normal')

    # Update the Random Number Generator list to store a list of 4 random unrepeated numerical values ranging from 0 to 6 (exclusively) 
    # Each of the 4 numbers represent a unique randomly generated colour our of the 6 options ('red', 'blue', 'green', 'yellow', 'pink', 'cyan')
    rng_colourSequence = random.sample(range(0, 6), 4)

    # Update the generated colour pattern list to the 4 colours selected by the random colour sequence
    # The unique generated numbers above will correspond to a unique index in the list of colours declared in the main program 
    # This list will contain the computer's generated code (the answer) that the user must crack
    generatedColourPattern = [color_list[rng_colourSequence[0]], color_list[rng_colourSequence[1]], 
        color_list[rng_colourSequence[2]], color_list[rng_colourSequence[3]]]
    print(generatedColourPattern)
    '''
    # Using a for counted loop, iterate as many times as there are indices in the list of 2D game buttons at the current row
    # The code will repeat in accordance with the number of columns there are in the current row (The length of the row)
    # This will ensure that the 2D list declared in the main program containing the game buttons for the user are each manipulated (4 buttons since the code is 4 colours) and only in the current row 
    # The current row should be the last row as the first attempt should start at the bottom and with each attempt, the row higher will be activated
    '''
    for column in range(len(list2DGameButtons[row])):
        '''
        # Update and configure the 2 dimensional list at the current row (the last row) and column (Each of the four buttons in the row)
        # The state must be changed to normal so that the user can beginning clicking and cycling through the colours of the buttons to begin their attempt
        # The relief must be set to raised to display a visual indicator that the following buttons are active and can be used to play
        # Set the background colour of the button to the tuple of colours declare in the main program at the index of its length - 1 or last index 
        # (The last item on the tuple - light gray - default colour)
        '''
        list2DGameButtons[active_row][column].config(state='normal', relief='raised', background=color_list[len(color_list) - 1]) 
    
    # Update and configure the message label by altering the text to tell the user to select 4 colours for the active buttons (Instructions to play)
    lblMessage.config(text='Select four (4) colours')  

# Define a function that will handle the events when any of the game buttons within the 4x15 2D list of buttons are clicked (Buttons displaying user's colour sequence guessing attempts)
# 2 Parameters will contain the row and column of the 2D list button selected to handle the colour changing events of that specific button
def game_buttons_command(row, col):

    # Declare the following variables and lists as global variables and lists 
    # These variables and lists may now be accessed and manipulated within the current function
    global active_row, list2DGameButtons, listCurrentButtonColours, listNumClicks

    # Check if the row of the button being checked is equivalent to the currently active row
    # This ensures that only the row in which the user is playing on is the only row being manipulated
    if row == active_row:

        # Update and configure the list of 2 dimensional game buttons at the current row and column being clicked 
        # Change the background colour to the color list tuple at the index of the list of number of clicks at the current column
        list2DGameButtons[row][col].config(background=color_list[listNumClicks[col]])

        # Update the list containing the current colour of the current row's buttons to the same colour set in the background of the current selected button
        listCurrentButtonColours[col] = color_list[listNumClicks[col]]

        # Increment the list of number of clicks at the index of the current column by 1
        listNumClicks[col] = listNumClicks[col] + 1

        # Check if the list of number of clicks at the index of the current column is equivalent to 7 (Out of index of colour list)
        if listNumClicks[col] == 7:

            # Return the value of the list of number of clicks at the current index of the current column to 0 (Re-start the cycle from the beginning as the end of the tuple has been reached)
            listNumClicks[col] = 0

# Define a function that will handle the events when the user confirms their attempt - Handles the events when the user clicks the submit button on the interface    
def confirm_attempt():

    # Declare the following variables and lists as global variables and lists 
    # These variables and lists may now be accessed and manipulated within the current function
    global active_row, listCurrentButtonColours, listNumClicks, attempts, numCorrectColours, numCorrectLocation, color_list, row
    global listCurrentButtonColours, rng_colourSequence, generatedColourPattern

    # Check if the amount of the colour at the last index (length colour index - 1) of the list of current button colours is greater than 0 
    # This essentially checks if any of the buttons are light-gray (default colour)
    if listCurrentButtonColours.count(color_list[len(color_list) - 1]) > 0:
        
        # Display a messagebox error that warns the user that they must select 4 colours before clicking the submit colour (Their choice is invalid)
        messagebox.showerror("Error", "You must select four (4) colours before selecting SUBMIT!")    

    # Otherwise, if the user has entered a valid attempt, execute the code below
    else:
        print(listCurrentButtonColours)
        print(generatedColourPattern)
        # Using a counter for loop, iterate through the computer's generated colour pattern code that it created above
        # Also, keep track of the current index using the enumerate function
        for index, colour in enumerate(generatedColourPattern):

            # Check if the amount of the current colour within the current button colours list is greater than 0
            # This means that if true, one or more of the user's colour options are included in the list
            if listCurrentButtonColours.count(colour) > 0:

                # Increment the variable storing the number of correct colours inputted by the user by 1
                numCorrectColours = numCorrectColours + 1

                # Check if that same colour (the list of generated colour patterns at the current index) is equivalent to the list of current button colours at the same index
                # This identifies whether this correct colour that the user chose is also at the correct position according to the pattern generated by the random number generator
                if generatedColourPattern[index] == listCurrentButtonColours[index]:

                    # Increment the variable storing the number of colours at their correct location by 1
                    numCorrectLocation = numCorrectLocation + 1

        print(numCorrectColours, numCorrectLocation)

        # Update and configure the list of labels beside the 2D list of buttons storing the amount of correct colours and locations at the current row and column being clicked 
        # Change the text within the label at the currently active row (beside the activated buttons) to display the number of correct colours the user chose and how many of them are in their designated location
        listGameInfoLabels[active_row].config(text=(str(numCorrectColours) + ", " + str(numCorrectLocation)))

        # Update and configure the message label at the bottom of the interface by altering the text to inform the user regarding the statistics of their submitted attempt 
        # Let them know how many colours they got correctly and how many colours in the correct location
        lblMessage.config(text=(str(numCorrectColours) + " colour(s) correct\n" + str(numCorrectLocation) + " colour(s) in the correct location"))

        '''
        # Using a for counted loop, iterate as many times as there are indices in the list of 2D game buttons at the current row
        # The code will repeat in accordance with the number of columns there are in the current row (The length of the row)
        # This will ensure that the 2D list declared in the main program containing the game buttons for the user are each manipulated (4 buttons since the code is 4 colours) and only in the current row 
        # The current row should be the last row as the first attempt should start at the bottom and with each attempt, the row higher will be activated
        '''
        for column in range(len(list2DGameButtons[row])):

            # Update and configure the list of 2 dimensional game buttons at the current row and column being clicked 
            # Change the state to disabled and the relief to sunken as this current row has already been used for the past attempt - Indicates that the row of buttons is now not open for use
            list2DGameButtons[active_row][column].config(state='disabled', relief='sunken') 

        # Check if either the number of correct colours and correct colour locations are equivalent to 4 or the attempts variable is equivalent to 15
        # This suggests that the game is over and the user has either won by getting the pattern in 15 or less attempts or they have not guessed the pattern after 15 attempts and they have lost
        if (numCorrectColours == 4 and numCorrectLocation == 4) or attempts == 15:

            # Condition if the user wins and guesses the correct pattern
            # Check if the number of correct colours and the number of correct colour locations are equivalent to 4
            if numCorrectColours == 4 and numCorrectLocation == 4:

                # Display a messagebox informing the user that they won by cracking the code along with how many attempts it took them
                messagebox.showinfo("You win!", 
                    "Congratulations...you cracked the code!\nIt took you " + str(attempts) + " attempt(s).")

            # Condition if the user losses and has expended all 15 of their attempts instead without guessing the pattern
            # Otherwise, check if the number of attempts is equivalent to 15
            elif attempts == 15:

                # Declare and initialize an empty string variable that will store the correct pattern that the user did not guess
                # This variable will store information to be displayed on a messagebox
                showUserPattern = ""

                # Using a counted for loop iterate through each colour item within the computer generated random colour pattern list
                # Also, keep track of the current index using the enumerate function
                for index, colour in enumerate(generatedColourPattern):

                    # Check if the current index is equivalent to 3 (Last item on the generatedColourPattern list)
                    if index == 3:

                        # Update the value of user pattern value by adding the current colour uppercased followed by a period
                        # This is its own condition because this is the last colour in the list so the sentence must end with a period
                        showUserPattern = showUserPattern + colour.upper() + "."

                    # Otherwise, execute the code below - This is not the (3rd) last index
                    else:

                        # Update the value of user pattern value by adding the current colour uppercased followed by a comma
                        showUserPattern = showUserPattern + colour.upper() + ", "

                # Diplay a messagebox that informs the user that they lost and have failed to crack the code - Use the variable created in the for loop above to display the correct pattern
                messagebox.showinfo("You lose!", 
                    "GAME OVER!\nYou failed to crack the code.\n\nThe code was " + showUserPattern)
            
            # Whether the user has won or lost, create a variable that stores the yes or no boolean variable and prompt the user using a messagebox with yes or no buttons 
            # Ask them whether they would like to play again - Store yes as True and no as False
            user_Choice_PlayAgain = messagebox.askyesno("Mastermind", "Would you like to play again?")

            # Check if the variable storing the user's messagebox option to play again is equivalent to True - User has indicated they want to play again
            if user_Choice_PlayAgain == True:

                # Re-initialize all basic game variables, lists, and any other components to restore the game interface and properties to their original state as if the program has just been started
                # See main program for information on the variables, list and components below
                attempts = 0
                active_row = 14
                numCorrectColours = 0
                numCorrectLocation = 0
                color_list = ('red', 'blue', 'green', 'yellow', 'pink', 'cyan', 'lightgray')
                rng_colourSequence = []
                generatedColourPattern = []
                listNumClicks = [0] * 4
                listCurrentButtonColours = [color_list[len(color_list) - 1]] * 4
                for row in range(len(list2DGameButtons)):
                    for column in range(len(list2DGameButtons[row])):
                        list2DGameButtons[row][column].config(state='disabled', background=color_list[len(color_list) - 1], relief='groove')
                for label in range(len(listGameInfoLabels)):
                    listGameInfoLabels[label].config(text="")
                btnStart.config(state='normal')
                btnSubmit.config(state='disabled')
                lblMessage.config(text='Click START to begin!')

            # Otherwise, the user has indicated that they would not like to play gain by selecting the no button in which case, the code below will execute
            else:
                # Thank the user through a messagebox for playing Mastermind before exiting
                messagebox.showinfo("Mastermind",
                    "Thank you for playing Mastermind!")

                # Terminate the program
                exit()

        # Otherwise, the user has not won nor lost the game as they have not gotten all for colours right along with their locations nor have they expended all of their attempts
        # In this case, execute the code below
        else:

            # Decrement the active row variable for the 2D list of Buttons by 1 so that the next row going up may be activated to commence the next attempt
            active_row = active_row - 1

            # Increment the number of attempts variable by 1 as the user is going on to their next attempt
            attempts = attempts + 1
            print(attempts)
            # Re-initialize the list storing the number of clicks to 4 values of 0 
            listNumClicks = [0] * 4

            # Re-initialize the number of correct colours to 0 
            numCorrectColours = 0

            # Re-initialize the number of correct colours in their correct locations to 0
            numCorrectLocation = 0

            # Re-initialize the list storing the user's current selection for each of the four buttons' colours to the last item (Length of colour list minus 1) on colour list (light gray default button colour - No selection made yet)
            listCurrentButtonColours = [color_list[len(color_list) - 1]] * 4

            '''
            # Using a for counted loop, iterate as many times as there are indices in the list of 2D game buttons at the current row
            # The code will repeat in accordance with the number of columns there are in the current row (The length of the row)
            # This will ensure that the 2D list declared in the main program containing the game buttons for the user are each manipulated (4 buttons since the code is 4 colours) and only in the current row 
            # The current row should be the last row as the first attempt should start at the bottom and with each attempt, the row higher will be activated
            '''
            for column in range(len(list2DGameButtons[row])):
                # Initialize the properties of the button of each column list of 2D games buttons at the current row
                '''
                # Update and configure the 2 dimensional list at the current row (the last row) and column (Each of the four buttons in the row)
                # The state must be changed to normal so that the user can beginning clicking and cycling through the colours of the buttons to begin their attempt
                # The relief must be set to raised to display a visual indicator that the following buttons are active and can be used to play
                # Set the background colour of the button to the tuple of colours declare in the main program at the index of its length - 1 or last index 
                # (The last item on the tuple - light gray - default colour)
                '''
                list2DGameButtons[active_row][column].config(state='normal', relief='raised', background=color_list[len(color_list) - 1])
            

# Define a function that will close the program when the user clicks the close button at the top right of the screen or the exit button
def terminate_program():

    # Prompt the user through a messagebox verifying whether they would like to exit for sure
    # Store the yes or no answer in the following variable
    user_response = messagebox.askyesno("Mastermind", 
        "Are you sure you want to exit?")

    # If the user's response is "yes", this indicates that the variable is equal to the boolean value of True in which case the code below will execute
    if user_response == True:

        # Thank the user through a messagebox for playing Mastermind before exiting
        messagebox.showinfo("Mastermind",
            "Thank you for playing Mastermind!")

        # Terminate the program
        exit()

# Declare two constants resembling the width and the height of the Tk surface window (915x320)
WINDOW_WIDTH, WINDOW_HEIGHT = 320, 915

# Create a Tk window that will display all objects for the graphical user interface
root = Tk()

# Set the name of the title of the Tk Window on the top left corner to "Mastermind" (Name of the program)
root.title('Mastermind')

# Set the size and location of the window using the contants declared above and formatting techniques
# The following properties ensure that the window is centered based on the properties of itself and the user's screen
root.geometry(f'{WINDOW_WIDTH:d}x{WINDOW_HEIGHT:d}+{root.winfo_screenwidth() // 2 - WINDOW_WIDTH // 2:d}+{root.winfo_screenheight() // 2 - WINDOW_HEIGHT // 2:d}')

# Call the function that terminates the program when the top right x button is clicked
root.protocol("WM_DELETE_WINDOW", terminate_program)

# Declare and initialize an integer variable that will store the current attempt number of the user
attempts = 0

# Declare an integer variable the will store the currently active row within the 2D list of game buttons that are displayed along with the list of labels
# It starts at 14 since the game starts at the bottom of the interface and progresses upwards with every attempt
active_row = 14

# Declare and initialize an integer variable that stores the number of correct colours that the user has guessed from the computers generated sequence of colours
numCorrectColours = 0

# Declare and initialize an integer variable that stores the number of correct colours in the correct locations that the user has guessed from the computers generated sequence of colours
numCorrectLocation = 0

# Declare a tuple that stores all of the colours that will be used within the game
color_list = ('red', 'blue', 'green', 'yellow', 'pink', 'cyan', 'lightgray')

# Declare and initialize a list that will store all of the randomly generated numbers that will correspond to an index within the colour list above to generate a random colour
rng_colourSequence = []

# Declare and initialize a list that will store all of the randomly generated colours in accordance with the colour list using the randomly generated indices of rng_colourSequence
generatedColourPattern = []

# Declare and initialize a list of integers that will store 4 0s each corresponding with the number of clicks for each column button within the current row
# This will help determine which colours need to be outputted next
listNumClicks = [0] * 4

# Declare a list containing each button's current colour of the 4 buttons in the row
# Initialize it so that each button starts off light gray by assigning each of the items in the list with the last index of colour list (length list - 1)
listCurrentButtonColours = [color_list[len(color_list) - 1]] * 4

# Declare and initialize a 2 dimensional list of None values that will eventually contain button objects for the game
# Will allow user to alter colours of each button
list2DGameButtons = [[None for column in range(4)] for row in range(15)]

# Declare and initialize a 1 dimensional list of None values that will eventually contain label objects for the game - Display numCorrectColours and numCorrectLocation
listGameInfoLabels = [None for label in range(15)]

# Create a Frame object that will allow us to place objects on and will be placed on the surface Window
# Contains all the main general components of the program - Will contain sub frames
# Will adjust its size based on dimensions of objects on it due to pack function
frame = Frame(root, padx=10, pady=20)
# Place the main frame on the main surface Window
frame.pack()

# Store a file containing an image of the mastermind main title logo
imgLogo = PhotoImage(file='images/mastermind.png')

# Create a label object that contains the mastermind image retrieved above
lblTitle = Label(frame, image=imgLogo, border=0)
# Output the label onto the main frame at the top
lblTitle.pack(side='top')

# Create a Frame object that will allow us to place objects on and will be placed on the main frame 
# Dedicate for main game components such as game buttons and labels
# Contains all the main general components of the program
# Will adjust its size based on dimensions of objects on it due to pack function
gameFrame = Frame(frame, pady=10)
# Output the game frame on the top most area of the main frame (Under title label)
gameFrame.pack(side='top')

# Will iterate through each item on the 2 dimensional game buttons list to ensure all their events are being handled 
# Using a counted for loop, iterate based on the number of rows within the 2 dimensional game buttons list (length of 2D list game buttons)
for row in range(len(list2DGameButtons)):

    # Using a for loop, iterate based on the number of columns within each row of the 2 dimensional game buttons list (length of 2D list game buttons at each row index)
    for column in range(len(list2DGameButtons[row])):

        # Create a de-activated button object at the current row and column that will handle the colour changing events of its individual self 
        # These buttons will be responsible for the functioning of the main game as the user will use these buttons to select their preference of colours for each of their attempts 
        list2DGameButtons[row][column] = Button(gameFrame, width=5, height=2, state='disabled', 
            relief='groove', background=color_list[len(color_list) - 1], command=lambda row=row, col=column: game_buttons_command(row, col))
        # Place the button object on an imaginary grid at their corresponding column and row as per their position on the 2 dimensional list
        list2DGameButtons[row][column].grid(row=row, column=column, padx=1, pady=1)

# Using a counted for loop, iterate based on the number of labels within the 1 dimensional list of game labels (length of 1D list of labels)
for label in range(len(listGameInfoLabels)):
    
    # Create a label object that will store statistics about the game regarding how many colours the user entered correct and how many are in their correct location within the attempt
    listGameInfoLabels[label] = Label(gameFrame, width=5, height=2, borderwidth=1, relief='solid', background='White')
    # Place the label on an imaginary grid so that the row corresponds with the position on the 1D list but the column is 4 so the labels are placed to the right of the 4x15 buttons
    listGameInfoLabels[label].grid(row=label, column=4, padx=1, pady=1, ipady=3, ipadx=3)

# Create a Frame object that will allow us to place objects on and will be placed on the main frame 
# Dedicate for Start, submit and quit command buttons
# Contains all the main general components of the program
# Will adjust its size based on dimensions of objects on it due to pack function
buttonFrame = Frame(frame, pady=20)
# Output the game frame on the top most area of the main frame (Under game frame)
buttonFrame.pack(side='top')

# Create a button object that will handle the events when the user clicks the start button - initializes components and begins first attempt
btnStart = Button(buttonFrame, text='START', width=10, command=commence_game)
# Output the button on the left of button frame
btnStart.pack(side='left', padx=3)

# Create a button object that will handle the events when user clicks the submit button - Main button that controls the conditions during the game as the user enters guesses
btnSubmit = Button(buttonFrame, text='SUBMIT', width=10, state='disabled', command=confirm_attempt)
# Output the button on the left of the button frame to the right of the start button
btnSubmit.pack(side='left', padx=3)

# Create a button object that will handle the events when the user clicks the quit button and wishes to exit the game
btnQuit = Button(buttonFrame, text='QUIT', width=10, command=terminate_program)
# Output the button on the left of the button frame to the right of the submit button
btnQuit.pack(side='left', padx=3)

# Create a message object that will store main instructions and statistics regarding the game - It will start by telling the user to click the start button to begin playing
lblMessage = Message(frame, text='Click START to begin!', font='TkDefaultFont 10 bold', pady=10, width=300, anchor='c')
# Output the message object on the top under currently existing objects
lblMessage.pack(side='top', fill='x')

# Main loop will listen for events triggered by the user and keep the program running
root.mainloop()