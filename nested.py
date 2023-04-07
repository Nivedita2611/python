from turtle import *
speed(10)

fillcolor('yellow')
pencolor('green')
side = 6
for i in range(side):
    fd(150)
    for i in range(side):
        fd(150)
        begin_fill()
        for i in range(side):
            fd(50)
            dot(10)
            for i in range(side):
                fd(25)
                lt(360/side)
            lt(360/side)    
            end_fill()
        lt(360/side)
    rt(60)

hideturtle()
mainloop()