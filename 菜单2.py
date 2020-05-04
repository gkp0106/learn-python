dict_menu={'面条':12,'米饭':1,'蛋炒饭':15,'水饺':9}
print("所有主食的平均价格为：",sum(dict_menu.values())/len(dict_menu),'元')
for items in dict_menu.items():
    if items[1]==max(dict_menu.values()):
        print("价格最高的主食是：",items[0])