import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Time is up!')

def start_countdown():
    print("请选择倒计时时间：")
    print("1. 1分钟")
    print("2. 3分钟")
    print("3. 5分钟")
    print("4. 自定义时间")
    choice = input("请输入选项号码: ")

    if choice == '1':
        t = 1 * 60
        countdown(t)
    elif choice == '2':
        t = 3 * 60
        countdown(t)
    elif choice == '3':
        t = 5 * 60
        countdown(t)
    elif choice == '4':
        custom_time = input("请输入自定义时间（分钟）: ")
        t = int(custom_time) * 60
        countdown(t)
    else:
        print("无效的选项")

if __name__ == '__main__':
    start_countdown()
