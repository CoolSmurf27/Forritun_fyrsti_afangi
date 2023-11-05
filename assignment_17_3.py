# Define your class "Hangman" here
class Hangman():
    def __init__(self, word: str):
        self.word = word.upper()
        self.revealed = [False] * len(word)
        self.incorrect_guesses = 0

    def guess_letter(self, letter: str) -> bool: 
        letter = letter.upper()
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.revealed[i] = True
            return True
        else:
            self.incorrect_guesses += 1
            return False
           
    def __str__(self) -> str:
        revealed_word = [letter if revealed else '_' for letter, revealed in zip(self.word, self.revealed)]
        return ' '.join(revealed_word) + '\nNumber of incorrect guesses: ' + str(self.incorrect_guesses)



