s = "钟山风雨起苍黄，百万雄师过大江。虎踞龙盘今胜昔，天翻地覆慨而慷。宜将剩勇追穷寇，不可沽名学霸王。天若有情天亦老，人间正道是沧桑。"
s =s.replace("，","/")
s=s.replace("。","/")
ls=s.split("/")
ls.remove("")
for i in range(0,len(ls),2):
    ls[i]=ls[i]+"。"+"\n"
for i in range(1,len(ls),2):
    ls[i] = ls[i] + "，"
ls.reverse()
s="".join(ls)
print(s)



