dict_menu={'面条':'12元','米饭':"1元",'蛋炒饭':'15元','水饺':'9元'}
total=0
price=[]
for i in dict_menu.values():
    m = [x for x in i if x.isdigit()]
    n = ''.join(m)
    price.append(int(n))
    total+=int(n)
print("所有主食平均价格为：",total/len(dict_menu),'元')
price=str(max(price))+"元"
for items in dict_menu.items():
    if items[1]==price:
        print("价格最高的主食是：",items[0])