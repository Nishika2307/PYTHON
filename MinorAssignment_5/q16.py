'''
Given the sets {10, 20, 30} and {5, 10, 15, 20}, use the mathematical set operators to produce the
following sets: a) {30}, b) {5, 15, 30} c) {5, 10, 15, 20, 30} d) {10, 20}
'''
set1={10,20,30}
set2={5,10,15,20}
sm=set1-set2 #differnce
print(sm)
sd=set1^set2 #symmetric differnce
print(sd)
u=set1|set2 #union
print(u)
i=set1 & set2 #intersection
print(i)
'''
{30}
{5, 30, 15}
{20, 5, 10, 30, 15}
{10, 20}
'''
