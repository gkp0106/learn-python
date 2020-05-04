class Solution:
    #最后mark数组里面标记的是皇后的位置，例如mark[0] = 2, 表示第一行皇后放在第3列的位置
    def make(self, mark):
        #初始化数组
        r = [['.' for _ in range(len(mark))] for _ in range(len(mark))]
        #将每一行中皇后的位置用‘Q’代替
        for i in mark:
            r[i][mark[i]] = 'Q'
        #枚举，将原来散的元素连接成字符串
        for k, v in enumerate(r):
            r[k] = ''.join(v)
        return r

    #递归函数，核心
    def recursive(self, mark, cur, ret):

        #如果当前行是最后一行，记录一个解，并返回上一级调用，继续探测
        if cur == len(mark):
            ret.append(self.make(mark))
            return

        #试探处理，将当前行的皇后应该在的位置遍历每一列，如果满足条件，递归调用处理下一行
        for i in range(len(mark)):
            mark[cur], down = i, True
            for j in range(cur):
                if mark[j] == i or abs(i-mark[j]) == cur - j:
                    down = False
                    break
            if down:
                self.recursive(mark, cur+1, ret)

    def solveNQueens(self, n):

        ret = []
        self.recursive([None]*n, 0, ret)
        return ret

enity = Solution()
print enity.solveNQueens(4)
