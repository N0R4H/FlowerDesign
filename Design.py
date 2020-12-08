import turtle as t
import random
t.getscreen()
t.title("Flower inception")
t.speed(100)
t.bgcolor("yellow")
t.pensize(3)
color_choice = ["black","blue","red","green"]
numbers = [20*x for x in range(20)]
def flower(l):
        if l==0:
            return "Deine Design ist abgeschlossen"
        #x = random.choice(numbers)
        #y = random.choice(numbers)
        #t.penup()
        for i in range(8):
              t.color(random.choice(color_choice))
              #t.setpos(x,y)
              t.pendown()
              t.rt(45)
              t.fd(l)
              t.rt(45)
              t.fd(l)
              t.bk(l)
              t.lt(90)
              t.fd(l)
              t.penup()
              t.setpos(0,0)
              t.rt(45)
              t.pendown()
        l-=10
        return flower(l)

print(flower(50))
t.mainloop()
print("thanks for watching")
