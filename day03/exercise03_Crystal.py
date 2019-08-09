## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test file in the terminal and see your results.
def count_vowels(word):
    if not int:
        raise TypeError()
        print("This is not a word")
        return None
    else:
       return sum([j in ["a", "e", "i", "o", "u"] for j in [i for i in word]])

count_vowels(22)
