import random

#游戏介绍
print("欢迎参加“三盒游戏”，在这个游戏当中，我们有三个神秘的盒子，一个是奖励盒子，而另外两个则为惩罚盒子。"
      "你的任务就是通过智慧和运气，选择奖励盒子。")

switch = input("你是否熟悉游戏规则(y/n)：").lower()
while switch not in ['y', 'n']:
    switch = input("无效的输入，请回答'y'或'n'：").lower()

if switch == 'y':
    print("那就开始吧(●'◡'●)")

else:
    #讲解游戏规则
    print("首先，你需要从三个盒子中选择一个盒子，并记下自己的选择。"
          "在你做出选择之后，主持人会帮你排除另外两个盒子中的一个惩罚盒子。")
    print("这时，你将有一次换盒子的机会，是坚持最初的选择，还是换到另一个未被选择的盒子。"
          "在你做出选择后，主持人便会揭晓答案")
    print("游戏规则介绍完毕，开始咯(⑅•ᴗ•⑅)")

def monty_hall():
    # 1代表奖励，0代表惩罚
    doors = [0, 0, 1]
    random.shuffle(doors)  # 随机分配
    print("在你面前有三个盒子，其中一个是奖励盒子，另外两个是惩罚盒子。")

    # 首次选择
    choice = int(input("请选择一个盒子（1、2或3）："))
    while choice < 1 or choice > 3:
        choice = int(input("无效的选择，请重新选择一个盒子（1、2或3）："))

    # 主持人排除一个惩罚盒子
    for i in range(3):
        if i + 1 != choice and doors[i] == 0:
            revealed = i + 1
            break

    print(f"主持人帮你排除了一个惩罚盒子，它是{revealed}号盒子。")

    # 是否更换选择
    switch = input("你是否想要更换你的选择？(y/n)：").lower()
    while switch not in ['y', 'n']:
        switch = input("无效的输入，请回答'y'或'n'：").lower()

    if switch == 'y':
        # 用户更换选择
        for i in range(1, 4):
            if i != choice and i != revealed:
                new_choice = i
                break
    else:
        # 坚持最初的选择
        new_choice = choice

    # 结果
    if doors[new_choice - 1] == 1:
        print(f"恭喜你！(✧∇✧) 你赢得了奖励！你选择了{new_choice}号盒子，它是奖励盒子。")
    else:
        print(f"很遗憾 Q_Q  你选择了{new_choice}号盒子，它是惩罚盒子。")

    input("结束啦，按回车键退出程序")
# 运行程序
monty_hall()