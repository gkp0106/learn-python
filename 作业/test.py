while 1:
    score = input("请输入你的分数：")
    if score == "e":
        break
    else:
        score = int(score)
        grade = "S" if score == 100 else "A" if 90 <= score < 100 else "B" if 80 <= score < 90 else "C" if 60 <= score < 80 else "D" if score < 60 else print("输入错误")
        print(grade)