# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        # Turn the original word into a sorted list of letters
        sorted_word = sorted(self.word.lower())

        matches = []
        for candidate in word_list:
            if sorted(candidate.lower()) == sorted_word:
                matches.append(candidate)

        return matches