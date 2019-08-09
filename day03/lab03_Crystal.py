import string
## 1. write tests in lab03_tests.py
## 2. then code for the following functions

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int


## make all characters capitalized
def shout(txt):
    print(txt.upper())
 

## reverse all characters in string
def reverse(txt):
    return txt[::-1]

## reverse word order in string
def reversewords(txt):
    print(reverse(txt.split()))

## reverses letters in each word
def reversewordletters(txt):
   words = txt.split()
   print(words)
   print([i[::-1] for i in words])
   

		
## change text to piglatin.. google it! 
#def piglatin(txt):
  #  if txt[0] in ["A" , "E" , "I" , "O" , "U"]:
   #     print("Vowell")
    #elif txt[1] in ["A" , "E" , "I" , "O" , "U"]:
     #   print("Vowell")
    #else txt[2] in ["A" , "E" , "I" , "O" , "U"]:
     #   return("Vowell")
    





## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
#string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]


#shout("yell")		
#reverse("opposite")			
#reversewords("Here are some words")			
#reversewordletters("Here are more words")			
#piglatin("Apple")			
			
			

