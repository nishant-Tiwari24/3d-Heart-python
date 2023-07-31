from turtle import *
import math

def heart(k):
    return 15*math.sin(k)**3
def heartbreak(k):
    return 12*math.cos(k)-5*math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)


speed(0)
bgcolor("black")
for i in range(6000):
    goto(heart(i)*20, heartbreak(i)*20)
    for j in range(5):
        color("red")
    goto(0,10)
done()