import random


# Creating lists

A=list()
B=list()
C=list()
D=list()
E=list()
F=list()
G=list()
H=list()

# Dict with all lists
decks = {
        'A':A, 'B':B, 'C':C, 'D':D,
        'E':E, 'F':F, 'G':G, 'H':H
        }

# Global run var
RUN = 1 

def menu():
        """
        Prints out a menu with available actions.
        :returns
        """
        print("""
---------------------------------------
1 - new game
2 - load game
3 - avslutt
---------------------------------------
""")
        choice = (input('Choose option:  '))
        if choice == '1':
            create_new_game()
            return True
        elif choice == '2':
                load_from_txt()

                # Checks that there is a game to play
                for deck in [A,B,C,D,E,F,G,H]:
                        if len(deck)>0:
                                return True
                        else:
                                new_game = input('The decks are all empty. Would you like to play a new game? (y/n):   ')
                                if new_game == 'y': 
                                        create_new_game()
                                else: 
                                        break
        elif choice == '3':
                quit()
        else:
                print('\nInvalid option. Try again.')
                menu()

def create_new_game():
        """
        Initiates a new game
        """

        card_values = ['7','8','9','10','J','Q','K','A']
        deck_of_cards = list()

        for val in card_values:
                deck_of_cards.append( '\u2660'+val) # spades
                deck_of_cards.append('\u2666'+val) # diamonds
                deck_of_cards.append('\u2663'+val) # clubs
                deck_of_cards.append('\u2665'+val) # hearts
        
        # Adds 4 random cards into the different decks
        for bunke in [A,B,C,D,E,F,G,H]:
            for n in range(0,4):
                kort = random.choice(deck_of_cards)
                bunke.append(kort)
                deck_of_cards.remove(kort)

def load_from_txt(filename = "Wish_Solitaire.txt"):
        """
        Loads a game from a .txt-file.
        """
        list= []
        try:
                with open(filename, 'r', encoding = 'UTF-8') as infile:
                        doc1 = infile.readlines()
                        for line in doc1:
                                line = line.rstrip().split()
                                list.append(line)
                        # Iterated all lines and decks
                        for i in range(0,8):
                                for line in list[i]:
                                        [A,B,C,D,E,F,G,H][i].append(line)
        except: 
                print('File does not exist')

                                
                                
                        

def quit():
        """
        Stops the game.
        """
        global RUN
        RUN = 0
     
def save_game(filename = 'Wish_Solitaire.txt'):
        """
        Saves the game in a .txt file, and stops the current game
        """
        with open(filename, 'w', encoding = 'UTF-8') as file:
                for kort_liste in [A,B,C,D,E,F,G,H]:
                        for kort in kort_liste:
                            file.write(kort+' ')
                        file.write('\n')

        # Stops the loop
        global RUN
        RUN = 0

def print_decks():
    """
    Prints all the decknames, the topmost card, and the number of cards in each deck on each line.
    """
    print()
    string_list = []
    for character in 'ABCDEFGH':
        string_list.append('      '+character+' ')
    
    deck_char_string = ''.join(string_list)
    print(deck_char_string ,end='\n    ')

    # Prints the top card in each deck
    for deck in [A,B,C,D,E,F,G,H]:
        spaces_between = 1
        if len(deck)!=0 and len(deck[0])>2:
                # if the number of the card is 10 
                spaces_between -=1
        if len(deck)<1:
                # If the deck is empty
                spaces_between +=1
                print(' [0]',' '*spaces_between, sep='', end = '  ')
        else: 
                print('[',deck[0],']',' '*spaces_between,sep='', end = '   ')
    print()

    # Prints the amount of cards left in decks
    print('      ', end = '')
    for deck in [A,B,C,D,E,F,G,H]:
        print(str(len(deck)), end = '       ')
    print()


def win_or_loss():
        """
        Checks if the game is won (all decks are empty), or if there are any possible moves.
        If it's won, or if there are no possible moves it stops.
        :returns: bool - True = Stop game
        """
        # All decks are empty
        if sum([len(x) for x in [A,B,C,D,E,F,G,H]]) == 0:
                print('Gratulerer!','Du vant!',sep = '\n')
                return True    

        # Checks if there are two cards of same value on the upmost cards.
        upmost_cards_list=[x[0][1:] for x in [A,B,C,D,E,F,G,H] if len(x)>0]

        # Set has removed duplicates
        if len(set(upmost_cards_list)) == len(upmost_cards_list):
                print('You lost... ', 'Always look at the briiiiight side of life...',
                        '*optimistical out of tune whistling*', sep = '\n')
                return True

   

def game():
    print_decks()
    if win_or_loss():
        global RUN
        RUN = 0
        return
    
    print('Press <ENTER> for menu')
    user_input_decks = input('Choose two decks:  ').upper()

    # If valid input it will remove the upmost cards from the 2 decks
    if len(user_input_decks)== 2 and user_input_decks[0] in 'ABCDEFGH' and user_input_decks[1] in 'ABCDEFGH':
        deck1 = decks[user_input_decks[0]] 
        deck2 = decks[user_input_decks [1]]
        if (len(deck1)>0 and len(deck2)>0) and deck1[0][1:] == deck2[0][1:]:
            deck1.pop(0)
            deck2.pop(0)
        else: print('You chose invalid decks, wrong amount of decks, or chose two decks where the upmost cards did not match.')
      
    elif user_input_decks == '':
            print("""\nWrite 'save' to save the game in a file.
                Write 'quit' to stop the game.
                Other inputs will continue the game
                """)
            option = input('Choose an option:').lower()
            if option == 'save': 
                save_game()
            elif option == 'quit': 
                quit()         
    else:
        print ('Invalid input. Please enter a valid input in this format: AB')
        return
   


# Program running loop
if menu():
        while RUN == 1:
                game()


