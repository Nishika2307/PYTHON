while True:
    choice=input("enter your choice : ")
    if(choice=="exit"):
      print("end of program")
      break
    else:
       a=int(input("enter number a :"))
       b=int(input("enter number b :"))
       match(choice):
            case "+":
               print("sum:",a+b)
            case "-":
                print("difference:",a-b)
            case "*":
                print("multiply:",a*b)
            case "/":
                if(b!=0):
                  print("divide",a/b)
                else:
                  print("cannot divide by zero")
            case _:
                print("invalid choice")
                
                
'''
enter your choice : /
enter number a :23
enter number b :0
cannot divide by zero
enter your choice : gt
enter number a :4
enter number b :5
invalid choice
enter your choice : exit
end of program
'''                
