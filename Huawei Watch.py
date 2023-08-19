import turtle
import datetime

# 设置窗口
window = turtle.Screen()
window.bgcolor("white")
window.title("华为运动表盘")

# 设置画笔
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# 绘制表盘外框
pen.penup()
pen.goto(0, -200)
pen.pendown()
pen.circle(200)

# 绘制刻度
def draw_ticks(num_ticks, tick_length, angle):
    for _ in range(num_ticks):
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(angle)
        pen.forward(180)
        pen.pendown()
        pen.forward(tick_length)
        pen.penup()
        pen.goto(0, 0)
        pen.left(360 / num_ticks)

draw_ticks(12, 20, 0)  # 绘制小时刻度
draw_ticks(60, 10, 0)  # 绘制分钟刻度

# 获取当前时间
current_time = datetime.datetime.now()

# 绘制时针
pen.penup()
pen.goto(0, 0)
pen.setheading(90 - current_time.hour * 30 - current_time.minute * 0.5)
pen.pendown()
pen.forward(80)

# 绘制分针
pen.penup()
pen.goto(0, 0)
pen.setheading(90 - current_time.minute * 6)
pen.pendown()
pen.forward(120)

# 绘制秒针
pen.penup()
pen.goto(0, 0)
pen.color("red")
pen.setheading(90 - current_time.second * 6)
pen.pendown()
pen.forward(140)

# 隐藏画笔
pen.hideturtle()

# 关闭窗口
window.mainloop()
