import random
import time

mapping = {
    0: "O", 1: "A", 2: "F", 3: "B", 4: "D",
    5: "V", 6: "S", 7: "L", 8: "M", 9: "H"
}


def prompt_number():
    while True:
        try:
            num = int(input("请输入循环次数: "))
            if num <= 0:
                print("请输入大于0的整数")
            else:
                return num
        except ValueError:
            print("请输入整数")


def prompt_answer(n):
    while True:
        answer = input(f"请输入数字{n}对应的大写字母: ").upper()
        if answer in mapping.values():
            return answer
        else:
            print("请输入大写字母L, O, F, B, D, V, S, E, M, H中的一个")


def main():
    num = prompt_number()
    count = {key: 0 for key in mapping.keys()}
    correct_count = {key: 0 for key in mapping.keys()}
    spend_time = {key: 0 for key in mapping.keys()}
    total_time = 0
    for i in range(num):
        n = random.randint(0, 9)
        print("第{}次：".format(i + 1))
        start_time = time.time()
        answer = prompt_answer(n)
        end_time = time.time()
        time_cost = round(end_time - start_time, 2)
        spend_time[n] += time_cost
        total_time += time_cost
        if answer == mapping[n]:
            print("回答正确！")
            correct_count[n] += 1
        else:
            print("回答错误，正确答案为：", mapping[n])
        count[n] += 1

    overall_accuracy = round(sum(correct_count.values()) / num * 100, 2)
    overall_time_cost = round(total_time / num, 2)

    print("总共循环了{}次，你的记忆正确率为：{:.2f}%".format(num, overall_accuracy))
    print("每次回忆的平均花费时间为：{}秒".format(overall_time_cost))

    for key, value in count.items():
        accuracy = round(correct_count[key] /
                         value * 100, 2) if value > 0 else 0
        avg_time = round(spend_time[key] / value,
                         2) if value > 0 else '0.00'
        print("{}->{}的记忆情况：测试{}次，平均花费时间为{}秒，正确率为{:06.2f}%".format(
            key, mapping[key], value, avg_time, accuracy))


if __name__ == '__main__':
    main()
