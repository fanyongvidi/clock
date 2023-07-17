import turtle
import time

# 创建画布
canvas = turtle.Screen()
canvas.bgcolor("black")
canvas.setup(width=600, height=600)
canvas.tracer(0)

# 创建画笔
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

# 绘制时针
def draw_hour_hand(length):
    pen.penup()
    pen.goto(0, 0)
    pen.color("white")
    pen.setheading(90)
    pen.pendown()
    pen.forward(length)

# 绘制分针
def draw_minute_hand(length):
    pen.penup()
    pen.goto(0, 0)
    pen.color("white")
    pen.setheading(180)
    pen.pendown()
    pen.forward(length)

# 绘制秒针
def draw_second_hand(length):
    pen.penup()
    pen.goto(0, 0)
    pen.color("red")
    pen.setheading(270)
    pen.pendown()
    pen.forward(length)

# 绘制刻度
def draw_ticks():
    pen.penup()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("white")
    pen.pendown()
    pen.circle(210)
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):
        pen.forward(190)
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.goto(0, 0)
        pen.right(30)

# 更新时钟
def update_clock():
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    second = current_time.tm_sec

    # 清除之前的时钟
    pen.clear()

    # 绘制刻度
    draw_ticks()

    # 绘制时针
    draw_hour_hand(80 + (hour % 12) * 30 + minute / 2)

    # 绘制分针
    draw_minute_hand(120 + minute * 6)

    # 绘制秒针
    draw_second_hand(140 + second * 6)

    # 更新画布
    canvas.update()

    # 每隔1秒更新一次时钟
    canvas.ontimer(update_clock, 1000)

# 启动时钟
update_clock()

# 运行主循环
turtle.mainloop()
