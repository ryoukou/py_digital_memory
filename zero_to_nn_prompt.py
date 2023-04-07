import random
import time

# 定义映射字典
mapping_dict = {
    0: "O", 1: "A", 2: "F", 3: "B", 4: "D",
    5: "V", 6: "S", 7: "L", 8: "M", 9: "H"
}

# 打乱映射字典的键值对，使得映射关系随机
mapping_list = list(mapping_dict.items())
random.shuffle(mapping_list)
mapping_dict = dict(mapping_list)

# 定义数字与字母组合的映射字典
num_letter_dict = {}
for i in range(10):
    for j in range(10):
        num_letter_dict[str(i) + str(j)] = mapping_dict[i] + mapping_dict[j]

# 提示用户输入循环次数
count = int(input("请输入循环次数："))

# 定义变量存储结果
total_time = 0
total_correct = 0
num_time_dict = {}
num_correct_dict = {}

# 循环生成数字并测试
for i in range(count):
    num = str(random.randint(0, 99)).rjust(2, "0")  # 生成随机数字并补齐至两位
    start_time = time.time()  # 记录测试开始时间
    user_input = input("第{}/{}次:请输入{}对应的字母组合：".format(i+1, count, num))
    end_time = time.time()  # 记录测试结束时间
    cost_time = end_time - start_time  # 计算测试花费时间，单位为秒
    total_time += cost_time

    # 判断用户输入是否正确
    if user_input.upper() == num_letter_dict[num]:
        print("回答正确！")
        total_correct += 1
        num_correct_dict[num] = num_correct_dict.get(num, 0) + 1  # 更新数字对应的正确次数
    else:
        print("回答错误！正确答案为：{}".format(num_letter_dict[num]))

    num_time_dict[num] = num_time_dict.get(
        num, []) + [cost_time]  # 更新数字对应的花费时间列表

# 计算并输出结果
total_accuracy = total_correct / count * 100
total_avg_time = total_time / count
print("总正确率：{:.2f}%，平均花费时间：{:.2f}秒".format(total_accuracy, total_avg_time))

# 按数字分别输出正确率和平均花费时间
for i in range(100):
    num = str(i).rjust(2, "0")
    if num in num_time_dict:
        num_accuracy = num_correct_dict.get(
            num, 0) / len(num_time_dict[num]) * 100
        num_avg_time = sum(num_time_dict[num]) / len(num_time_dict[num])
        print("{}->{}对应的字母组合测试了{}次：正确率：{:.2f}%，平均花费时间：{:.2f}秒".format(
            num, num_letter_dict[num], len(num_time_dict[num]), num_accuracy, num_avg_time))
