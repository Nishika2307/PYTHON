'''
Write a function that takes a positive number as an input and converts the respective digits into corresponding
text. Example: 85 7→ eight five, 123 7→ one two three.'''

def towords(k):
  match k:
    case 0:
      return "zero"
    case 1:
      return "one"
    case 2:
      return "two"
    case 3:
      return "three"
    case 4:
      return "four"
    case 5:
      return "five"
    case 6:
      return 'six'
    case 7:
      return 'seven'
    case 8:
      return 'eight'
    case 9:
      return 'nine'

def answer(n):
  if(n==0):
    return ""
  else:
    return answer(n//10)+" "+towords(n%10)
  
n=int(input("enter a number : "))
print(answer(n))

'''
enter a number : 648
 six four eight'''
 