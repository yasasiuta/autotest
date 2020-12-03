import copy
import math
import time



# a = [1,2,3]
# b = [4,5,6]
# c = [a,b]
# print(c)
# d = copy.copy(c)
# e = copy.deepcopy(c)
# a.append([55])
# print(c)
# print(d)
# print(e)
#1.逐一显示列表l1= ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"] 中索引为奇数的元素
l1= ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
# l2 =(l1[1::2])
# for i in l2:
#     print(i)
# for i in range(len(l1)):
#     if i % 2 != 0:
#         print(l1[i])

# 2.将属于列表l1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]，
# 但不属于列表l2 = ["Sun","Mon","Thu","Fri","Sat"]的所有元素定义为一个新列表l3
l1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
l2 = ["Sun","Mon","Thu","Fri","Sat"]
l3 = []

for i in l1:
    if i not in l2:
        l3.append(i)
print(l3)


# 3.已知列表namelist=['stu1','stu2','stu3','stu4','stu5','stu6','stu7']，删除列表removelist=['stu3', 'stu7', 'stu9']；
# 请将属于removelist列表中的每个元素从namelist中移除(属于removelist，但不属于namelist的忽略即可)；

namelist=['stu1','stu2','stu3','stu4','stu5','stu6','stu7']
removelist=['stu3', 'stu7', 'stu9']
for i in removelist:
    if i in namelist:
        namelist.remove(i)

print(namelist)

#4.有一个字符串是一句英文，统计每个单词出现的次数，生成一个字典，单词作为key，次数作为value生成一个字典dict1
str1 = "today is a good day today is a bad day today is a nice day"
dict = {}

l1 = str1.split(" ")
print(l1)
for i in l1:
    num = l1.count(i)
    dict[i] = num
print(dict)

# 5.已知列表list1 = [0,1,2,3,4,5,6],list2 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"],
# 以list1中的元素作为key，list2中的元素作为value生成一个字典dict2

list1 = [0,1,2,3,4,5]
list2 = ["Sun","Mon","Tue","Wed","Thu","Fri"]
dict = {}
for i in range(len(list1)):
    dict[list1[i]] = list2[i]
print(dict)


#可以用集合去除列表中的重复元素
# l1 = [1,2,3,4,4,5,1,2,8,9]
# l2 = set(l1)
# print(l2)
# l2.add(88)
# print(l2)
# l2.remove(1)
# print(l2)
# print(l2&set(l1))
# print(l2|set(l1))

# 简述：这里有四个数字，分别是：1、2、3、4
#
# 提问：能组成多少个互不相同且无重复数字的三位数？各是多少？
#
# Python解题思路分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
# count = 0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i != j and j != k and i != k :
#                 count += 1
#                 print(i,j,k)
#
# print(count)


# 简述：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
# 高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
# 高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成.
#
# 提问：从键盘输入当月利润I，求应发放奖金总数？ 玩蛇网Python解题思路分析：请利用数轴来分界及定位。
# 并要注意定义时需要把奖金定义成长整型的数据类型。

# x = int(input("请输入当月利润"))
# arr = [1000000,600000,400000,200000,100000,0]
# rate = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for i in range(len(arr)):
#     if x > arr[i]:
#         r += (x - arr[i])*rate[i]
#         x = arr[i]
#
# print(r)

# 简述：一个整数，它加上100和加上268后都是一个完全平方数
#
# 提问：请问该数是多少？ Python解题思路分析：在10000以内判断，将该数加上100后再开方，加上268后再开方，
# 如果开方后的结果满足如下条件，即是结果。 Python完全平方数，python解题源代码如下：
for i in range(1,10000):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+268))
    if (x*x == i+100) and (y*y == i+268):
        print(i)


# 简述：要求输入某年某月某日
#
# 提问：求判断输入日期是当年中的第几天？ Python解题思路分析： 我们就以3月5日这一天为例。
# 首先把前两个月的加起来，然后再加上5天即本年的第几天。这里有一种特殊的情况，就是闰月，
# 遇到这种情况且输入月份大于2时需考虑多加一天。如果不是很明白，可以看下边的python源码。

# 整数顺序排列问题简述：任意三个整数类型，x、y、z
#
# 提问：要求把这三个数，按照由小到大的顺序输出 Python解题思路分析：
#
# 首先，要想方法把最小的数放到x位上，之后将x与y进行比较； 如果x>y的话，就将x与y的值进行交换；
# 然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

l1 = [78,34,44,12]
l1.sort()
print(l1)

print(time.time())
print(time.localtime())
# print(time.strptime(time.localtime(time.time()),"%y-%m-%d %hh:%mm:%ss"))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


str = 'ghgh'
# print(str.find("crystal"))
# print(str.index("crystal"))
# print(str.rfind("crystal"))
# print(str.rindex("crystal"))
# newstr = str.replace("my","your")
# print(newstr)
s = str.split("、")
print(s)
print(str.capitalize())
print(str.title())
print(str.upper())
f = str.strip(",")
print(f)
k = str.ljust(30," ")
print(k)
print(str.isalnum())
print(str.isalpha())


namelist = ['crystal','jack','bill','nono 赣B01629、赣B01651、赣B01804']
namelist.remove('jack')
print(namelist)
i = 'crystal'
if i in namelist:
    print(namelist.index(i))
    print(namelist.count(i))
else:
    print('wobuzai')
print(namelist.pop())
print(namelist[1])
namelist.clear()
print(namelist)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list2.append(9)
print(list2)
list1.extend(list2)
print(list1)
list1.insert(2,99)
print(list1)
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

#集合

set1 = set()
set2 = {1,3,5,6,7}
set3 = set([1,9,10,3,6])
set1.add(999)
print(set1)
set1.update([2,4])
print(set1)
print(set2.pop())
set2.remove(3)
print(set2)
set2.discard(1)
print(set2)
print(set2|set1)
print(set2&set3)
print(set3 - set2)

#filter 过滤序列中不符合条件的元素 filter(函数名，可迭代对象)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,50,55,63,100]

def func(x):
    return  x%2 == 0

res = filter(func, lst)
print(list(res))

print(list(filter(lambda x: x%2 == 0,lst)))
print(filter(lambda x: x%2 == 0,lst))


#map(函数名，可迭代对象) 将可迭代对象的每一个值都作为函数的参数进行运算，然后将结果添加到一个新对象中返回
# 返回的是内存地址，需要用list（）进行转换

print(list(map(lambda x: x%2 == 0,lst)))

#reduce 把一个函数作用在一个序列上，函数必须接入两个参数，reduce把结果  继续和序列的下一个元素做累计运算
import functools
def fun(a,b):
    return a+b
res = functools.reduce(fun,lst)
print(res)


def test1(number1):
    print("____1____")
    number1 = number1+2
    print(number1)
    def test2():
        print("_____2____")
        number2 = number1+100
        print(number2)
    print("_____3______")
    return test2

res = test1(10)
res()














