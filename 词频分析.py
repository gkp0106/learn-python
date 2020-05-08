def filt(s: str):
    '''
    过滤字符串标点符号换行符
    '''
    x = ["\n",'!', '-', '.', ',', '?', ":", ";", '"', '\\']
    for i in s:
        for j in x:
            if j in i:
                s = s.replace(i, '')
    return s


l = ['bob', 'two', 'did', 'twenty', 'our', 'its', 'under', 'sometimes', 'just', "i'm", 'by', 'until', 'be', 'might',
     'or',
     'you', 'myself', "couldn't", 'it', 'had', 'them', 'with', 'of', 'at', "o'clock", '10', 'after', 'the', 'on', 'to',
     'up', 'and', 'not', 'for', 'were', 'am', 'but', 'are', 'since', 'been', 'when', 'where', 'what', 'a', 'an', 'ago',
     'was', 'i', 'he', 'she', 'we', 'they', 'my', 'their', 'her', 'his', 'him', 'jimmy', 'is', "he'll", 'will', "i'll",
     'as', 'along', 'there', 'now', 'in', 'that', 'then', "it's", "i'd", 'here', 'if', 'so', 'could', "you've", 'oh',
     'from']  # 一些无关词汇
with open(r'C:\Users\mayn\Desktop\编程\novel.txt', 'r') as f:
    x = f.readlines()
    m = list(map(filt, x))
    n = []
    for i in m:
        i = i.split(" ")
        for x in i:
            x = x.lower()
            if x == '':
                continue
            if x[0] == "'" and x[-1] == "'":  # 去除'word'的前后引号#
                x = x[1:-1]
            if "'" in x:  # 去除无关缩写词#
                continue
            n.append(x)
    for i in l:
        while i in n:
            n.remove(i)
    dict1 = dict()
    for i in set(n):
        a = n.count(i)
        dict1[i] = a
    b = [(x, y) for y, x in dict1.items()]
    b = sorted(b, reverse=True)
    result = ["%s 出现了 %d次\n" % (b[i][1], b[i][0]) for i in range(10)]
    with open(r'C:\Users\mayn\Desktop\编程\novel词频统计.txt', 'w') as g:
        g.writelines(result)
