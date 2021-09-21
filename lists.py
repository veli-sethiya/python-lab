Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list=[]
>>> list=[1,2,3]
>>> list1=[1,"hello",4.2]
>>> list1
[1, 'hello', 4.2]
>>> list1=[1,"hello",[1,4.2]]
>>> list1
[1, 'hello', [1, 4.2]]
>>> print(list1[-1:1])
[]
>>> list1.append(4)
>>> list1
[1, 'hello', [1, 4.2], 4]
>>> list1.append([1,4])
>>> list1.append(4)
>>> list1
[1, 'hello', [1, 4.2], 4, [1, 4], 4]
>>> list1[2]='r'
>>> list1
[1, 'hello', 'r', 4, [1, 4], 4]
>>> list1.append(1,2,3)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list1.append(1,2,3)
TypeError: list.append() takes exactly one argument (3 given)
>>> list1.extend([1,2,3])
>>> list1
[1, 'hello', 'r', 4, [1, 4], 4, 1, 2, 3]
>>> list1 + (1,2,3)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list1 + (1,2,3)
TypeError: can only concatenate list (not "tuple") to list
>>> list1 + [1,2,3]
[1, 'hello', 'r', 4, [1, 4], 4, 1, 2, 3, 1, 2, 3]
>>> print(["amit"]*3)
['amit', 'amit', 'amit']
>>> list1.insert(3,"amit patel")
>>> list1
[1, 'hello', 'r', 'amit patel', 4, [1, 4], 4, 1, 2, 3]
>>> list
[1, 2, 3]
>>> list=[1,3,4]
>>> list[1:1]=[9,93,44]
>>> list
[1, 9, 93, 44, 3, 4]
>>> list[1:3]=[9,93,44]
>>> list
[1, 9, 93, 44, 44, 3, 4]
>>> list.remove(44)
>>> list
[1, 9, 93, 44, 3, 4]
>>> list.pop()
4
>>> list
[1, 9, 93, 44, 3]
>>> list.clear()
>>> list
[]
>>> list=[11,3,4,2,5,6,4,5]
>>> list.count(4)
2
>>> 