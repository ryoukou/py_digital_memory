import random
import pyperclip

while True:
    n = input("请输入一个1~9999之间的数字：")
    try:
        n = int(n)
        if 1 <= n <= 9999:
            rand_num = ''.join([str(random.randint(0, 9)) for _ in range(n)])
            print("随机生成的数字为：", rand_num)
            pyperclip.copy(rand_num)
            print("已复制到系统剪贴板！")
        else:
            print("输入数字不在1~9999之间，请重新输入！")
    except KeyboardInterrupt:
        print("程序已退出！")
        break
    except ValueError:
        print("输入内容不是数字，请重新输入！")


# while True:
#     try:
#         n = int(input("请输入一个1~9999之间的数字："))
#         rand_num = random.randint(10**(n-1), 10**n-1)
#         print("随机生成的数为：", rand_num)
#         pyperclip.copy(rand_num)
#         print("已复制到剪贴板！")
#     except KeyboardInterrupt:
#         print("程序已退出！")
#         break
#     except ValueError:
#         print("输入有误，请重新输入！")
