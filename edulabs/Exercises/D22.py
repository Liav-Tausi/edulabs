import string

# Implement a simple class AlphabetIterator. The class should be initialized with a letter from the English Alphabet (uppercase or lowercase).
# If the class is not initialized with uppercase or lowercase English letters - your __init__ method should throw an exception!


class AlphabetIterator:

    def __init__(self, letter: str):
        if letter not in string.ascii_letters:
            raise Exception("char not in Alphabet.")
        self.letter: str = letter

    def __iter__(self):
        if self.letter in string.ascii_uppercase:
            self.counter = string.ascii_uppercase.index(self.letter)
        else:
            self.counter = string.ascii_lowercase.index(self.letter)
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > len(string.ascii_lowercase) - 1:
            raise StopIteration()
        if self.letter in string.ascii_uppercase:
            return string.ascii_uppercase[self.counter]
        else:
            return string.ascii_lowercase[self.counter]


if __name__ == "__main__":

    for i in AlphabetIterator("K"):
        print(i, end=" ")
