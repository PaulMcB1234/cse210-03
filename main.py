import random
# The puzzle is a secret word randomly chosen from a list.
# The player guesses a letter in the puzzle.
# If the guess is correct, the letter is revealed.
# If the guess is incorrect, a line is cut on the player's parachute.
# If the puzzle is solved the game is over.
# If the player has no more parachute the game is over.

# Class for director
# Class for image
# Class for guessing
# Class for words

class Director():
    # facilitates the game, 
    # keeps track of the guesses left, 
    # and if the game is playing,

    def __init__(self):
        self.is_playing = True
        self.guesses = 5
        self.word_list = []
        
    def make_word_list(self, words):
        self._word = words.word
        self.word_list = words.word.split(",")
        
    def start_game(self, image, guess, words):
        self.still_playing()
        words.pick_word()
        while self.is_playing:
            self.make_word_list(words)
            image.print_display(self.word_list)
            guess.get_input()
            guess.is_correct(self.word_list)
            self.guesses = guess.if_wrong(self.guesses, image)
            print(self.guesses)
            guess.if_right(self.word_list)
        
        
    def still_playing(self):
        # If the game has 0 guesses left or if the player wins, game over.
        if self.guesses == 0:
            #Implement a working quit
            self.is_playing = False

class Image():
    # display our stick man, our parachute, and our word count.

    def __init__(self):
        self.display_words = '_ _ _ _ _'
        self.display_parachute = {
            1:' ______ ',
            2:'/      \ ',
            3:'|      |',
            4:' \    /',
            5:'  \  /',
            6:'   o',
            7:'  /|\ ',
            8:'  / \ ',
            9:'',
            10:'^^^^^^'
        }
        
    def print_display(self, word_list):
        
        print(f"{word_list}")
        print(f"{self.display_parachute[1]}")
        print(f"{self.display_parachute[2]}")
        print(f"{self.display_parachute[3]}")
        print(f"{self.display_parachute[4]}")
        print(f"{self.display_parachute[5]}")
        print(f"{self.display_parachute[6]}")
        print(f"{self.display_parachute[7]}")
        print(f"{self.display_parachute[8]}")
        print(f"{self.display_parachute[9]}")
        print(f"{self.display_parachute[10]}")
        

class Guessing():
    # takes the input of the player, and tells the game if the input is or is not correct.
    def __init__(self):
        self.player_guess = ''
        self.correct = None
        self.word_list = []
        self._private_word_list = ""
        self._player_guess = ""

    def get_input(self):
        # take user input, change self.player_guess to input.
        self._player_guess = input("guess a letter [a-z]: ")

    def is_correct(self, word_list):
        # check to see if user input is correct, changes self.correct to TRUE or FALSE .
        
        #take list and compare guess to the list
        
        
        for i in word_list:
            if self._player_guess in word_list:
                self.correct = True
                break
            else:
                self.correct = False
                       
       
    
    def if_wrong(self, guesses, image):
        # Takes info from self.correct and determines what to do if the guess is wrong

        if self.correct == False:
            guesses -= 1
            #It isn't popping 0, it says it don't exist
            image.display_parachute.pop(0)
        return guesses
            
    
    def if_right(self, word_list):
        # Takes info from self.correct and determines what to do if the guess is right
        
        if self.correct == True:
            self._private_word_list = word_list
            for i in self._private_word_list:
                if i != self.player_guess:
                    i = "_"
                else:
                    pass
        for i in self._private_word_list:
            if i != "_":
                
                #i is not an integer, i is a string
                #This whole thing won't work quite how we want it either.
                word_list[i] = self._private_word_list[i]
        

class Words():
    # choose a random word out of out list.
      
    def __init__(self):
        self.word = []
        
    def pick_word(self):
        words = ['p,z,a,z,z', 'p,i,z,z,a', 'b,o,o,k,s', 'c,h,i,p,s', 'g,h,o,s,t', 'm,a,i,z,e', 'p,e,a,c,h', 'p,i,a,n,o', 'a,p,p,l,e']
        self.word = random.choice(words)
        

def main():
    
    image = Image()
    guess = Guessing()
    words = Words()
    game = Director()
    
    
    
    game.start_game(image, guess, words)
main()