class Hangman:

    def __init__(self, word):
        self.dicky = {}
        self.word = word

        for i in word:
            if i not in self.dicky:
                self.dicky[i] = 1
            else: self.dicky[i] = self.dicky[i] + 1

        self.output_list = []

        for i in word:
            self.output_list.append("_ ")

        self.play_game()

        while not self.check_underscore():
            self.output_list = take_a_guess(self.output_list)

        print("You win!")

    def play_game(self):
        self.print_letters()
        while not self.check_underscore():
            self.output_list = self.take_a_guess()
            self.print_letters()

            
    def print_letters(self):
        letters = ""
        for i in self.output_list:
            letters = letters + i
        print(letters)
        
    def check_underscore(self):
        for i in self.output_list:
            if i[0] == "_":
                return False
        return True

    def take_a_guess(self): #returns updated letters list
        print("Guess a letter: ")
        g = input().lower()

        if g in self.dicky: #if they guess correctly
            where_is_g = []
            for i in range(len(self.word)): #go through the word
                if g == self.word[i]:       #get all indexes of the occurrance 
                    where_is_g.append(i)    #put them in where_is_g

            #so g is in output list and we have to replace it with g
            for i in where_is_g:
                self.output_list[i] = g + " "
            return self.output_list
                
        else: return self.output_list







