
"""
n = 50
k = 12
s = "pkdsjlbnvqoykclgjippobahlxmlsgynxxokeongvdsusvmorh"
"""

权重字典 = {}
权重 = 1
for i in range(97 ,123):
    权重字典[chr(i)] = 权重
    权重 = 权重 + 1

# print(权重字典)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

s = "pkdsjlbnvqoykclgjippobahlxmlsgynxxokeongvdsusvmorh"

# 权重从小到大排序
sort_s = sorted(s)

# print(sort_s)
# ['a', 'b', 'b', 'c', 'd', 'd', 'e', 'g', 'g', 'g', 'h', 'h', 'i', 'j', 'j', 'k', 'k', 'k', 'l', 'l', 'l', 'l', 'm', 'm', 'n', 'n', 'n', 'o', 'o', 'o', 'o', 'o', 'p', 'p', 'p', 'q', 'r', 's', 's', 's', 's', 'u', 'v', 'v', 'v', 'x', 'x', 'x', 'y', 'y']

# 去重
set_sort_s = "".join(sorted(list(set(sort_s))))
# print(set_sort_s)
# abcdeghijklmnopqrsuvxy

def result(s):
    result = 0
    for i in s:
        result = result + 权重字典[i]
    return result

def loopSearch(set_sort_s, index, k):

    if len(set_sort_s)-1 >= index:
        _set_sort_s = set_sort_s
        temp_s = set_sort_s[index]
        for i in set_sort_s[index:]:
            if 权重字典[i] != 权重字典[temp_s[-1]] and 权重字典[i] != 权重字典[temp_s[-1]] +1:
                temp_s = temp_s + i
            if len(temp_s) == k:
                print(temp_s, result(temp_s))
                _set_sort_s = set_sort_s.replace(temp_s[-1], "")
                break

        if len(_set_sort_s) != len(set_sort_s):
            if len(temp_s) >= k:
                loopSearch(_set_sort_s, index, k)

def calc(s, k):
    # 权重从小到大排序
    sort_s = sorted(s)
    # print(sort_s)
    # ['a', 'b', 'b', 'c', 'd', 'd', 'e', 'g', 'g', 'g', 'h', 'h', 'i', 'j', 'j', 'k', 'k', 'k', 'l', 'l', 'l', 'l', 'm', 'm', 'n', 'n', 'n', 'o', 'o', 'o', 'o', 'o', 'p', 'p', 'p', 'q', 'r', 's', 's', 's', 's', 'u', 'v', 'v', 'v', 'x', 'x', 'x', 'y', 'y']
    # 去重
    set_sort_s = "".join(sorted(list(set(sort_s))))
    for index in range(len(set_sort_s)):
        loopSearch(set_sort_s, index, k)

if __name__ == "__main__":

    s = "pkdsjlbnvqoykclgjippobahlxmlsgynxxokeongvdsusvmorh"
    k = 12
    calc(s, k)

    # 都查找不到权重为-1，如下例：
    # k = 2
    # s = "ababab"
    # 输出 -1