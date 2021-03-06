## Trick and explanation of base conversion
## http://www.purplemath.com/modules/base_why.htm

"""convert positive integer to base 2"""

def binarify(num):
  remain = []
  while num != 0:
    remain.append(str(num % 2))
    num //= 2
  remain.reverse()
  return "".join(remain)

binarify(15)   

# take number and divide by 2 
# save whole number
# save remainder in string 
# make whole number new divisor 
# divide by 2
# repeat until remainder =0 

"""convert positive integer to a string in any base"""
def int_to_base(num, base):
  remain = []
  while num != 0:
    remain.append(str(num % base))
    num //= base
  remain.reverse()
  return "".join(remain)

int_to_base(15, 3)  

"""take a string-formatted number and its base and return the base-10 integer"""
def base_to_int(string, base):
  thenumber = len(string)-1 	
  while thenumber != 0: 	 
    basepower = base ** thenumber
    thenumber = thenumber-1
    basepower.append
 


"""add two numbers of different bases and return the sum"""
def flexibase_add(str1, str2, base1, base2):


"""multiply two numbers of different bases and return the product"""
def flexibase_multiply(str1, str2, base1, base2):


"""given an integer, return the Roman numeral version"""
def romanify(num):

  
# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.