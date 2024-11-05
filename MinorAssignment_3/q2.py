'''
Find the numbers between 100 and 500, which are divisible by 3 and multiples of 5 using function in
Python.
'''

def divisible(num):
    if(num%3==0 and num%5==0):
        return True
    else:
        return False



for i in range (100,501):
    if(divisible(i)):
        print(i,end=" ")
    
'''
105 120 135 150 165 180 195 210 225 240 255 270 285 300 315 330 345 360 375 390 405 420 435 450 465 480 495 
'''
