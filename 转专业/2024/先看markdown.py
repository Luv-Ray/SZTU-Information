def Q1():
    """
    1. 输入一行数字，输出最大值
    白给
    """

    print(max(input().split()))


def Q2():
    """
    2. 输入一行数字，输出平均值和高于平均值的数字
    还是白给
    """

    print(f"平均值为{sum(l := list(map(int, input().split()))) / len(l):.1f}\n高于平均值的为{[i for i in l if i > sum(l) / len(l)]}")
    # 看懂了就行千万别这样写，可读性爆炸


def Q3():
    """
    3. 输入一行数字，输出能排列成的最大数字

    力扣179.最大数
    https://leetcode.cn/problems/largest-number/

    可以把数字当成字符串来处理，x * 10 是为了让数字按位数排序
    """

    nums = sorted(input().split(), key=lambda x: x * 10, reverse=True)
    res = ''.join(nums).lstrip('0')
    print(res if res else '0')


def Q4(*args):
    n = int(args[0])
    x = args[1]
    m = int(args[2])
    CHAR_SET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    is_valid = True
    """
    4. 输入一个数字，转换成其他进制
    
    枫神把题目发在了洛谷
    洛谷U564501 图神的进制魔典
    https://www.luogu.com.cn/problem/U564501
    
    :param n: 原进制
    :param x: 非负整数
    :param m: 目标进制
    没有恶心的数据所以可以不用写那么多合法性检查
    """

    # try:
    #     x = str(x)
    # except:
    #     return "ValueError"
    #
    # if not (2 <= n <= 60 and 2 <= m <= 60):
    #     return "ValueError"

    if is_valid:
        for i in x:
            if i not in CHAR_SET[:n]:
                return "ValueError"

        dec = 0
        for i in x:
            dec = dec * n + CHAR_SET.index(i)

        res = ""
        while dec:
            res = CHAR_SET[dec % m] + res
            dec //= m

        return res

