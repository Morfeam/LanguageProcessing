# Matthew Morfea - 2/24/20
# Chapter 5 Question 1 parser

import sys   # needed to access command line arg

#global variables
tokenindex = -1
token = ''

def main():
   try:
      parser()      # call the parser
   except RuntimeError as emsg:
      print(emsg)

def advance():
   global tokenindex, token
   tokenindex += 1    # move tokenindex to next token
   # check for null string or end of string
   if len(sys.argv) < 2 or tokenindex >= len(sys.argv[1]):
      token = ''      # signal the end by returning ''
   else:
      token = sys.argv[1][tokenindex]

def consume(expected):
   if expected == token:
      advance()
   else:
      raise RuntimeError('Expecting ' + expected)

def parser():
   advance()   # prime token with first character
   S()         # call function for start symbol
   # test if end of input string
   if token != '': 
      print('Garbage following <S>-string')
   
def S():
   if token == 'a' or token == 'b' or token == 'c' or token == '':
      A()
      B()
      C()
      pass
   else:
      raise RuntimeError('Expecting a, b, c, or End of Input')
def A():
   if token == 'a':
      advance()
   elif token == 'b' or token == 'c' or token == '':
      pass
   else:
      raise RuntimeError('Expecting b, c, or End of Input')
def B():
   if token == 'b':
      advance()
   elif token == 'c' or token == '':
      pass
   else:
      raise RuntimeError('Expecting c or End of Input')
def C():
   if token == 'c':
      advance()
   elif token == '':
      pass
   else:
      raise RuntimeError('Expecting End of Input')
      
main()
