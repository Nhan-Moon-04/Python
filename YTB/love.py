import turtle

def draw_heart():
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(224)
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(224)
    turtle.left(120)
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(224)
    turtle.end_fill()

# Thiết lập màn hình
turtle.setup(width=800, height=600)
turtle.title("Trái tim ngầu và đẹp")
turtle.bgcolor('black')
turtle.speed(2)
turtle.hideturtle()
turtle.penup()

# Di chuyển đến vị trí vẽ trái tim
turtle.goto(0, -100)
turtle.pendown()

# Vẽ hình trái tim
draw_heart()

# Dừng chương trình khi nhấn vào màn hình
turtle.exitonclick()
