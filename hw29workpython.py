
def f1(x):
    return x*x

res = f1(5)
print(res)

nums = [1,2,3]
nums2=[]
for i in nums:
    t = f1(i)
    nums2.append(t)
print(nums2)


nums2 = list(map(lambda x: x*x,nums))
print(nums2)

n1 = [1,2,3]
n2 = [4,5,6]
n3 = list(map(lambda x,y: x*y,n1,n2))
print(n3)

m1 = ['cat','dof','parrot']
m2 = list(filter(lambda r: len(r)<=3,m1))
print(m2)

import random
numbers = []
for i in range(10):
    numbers.append(random.randint(10, 20))
numbers = list(filter(lambda x: x%5==0,numbers))
print(numbers)

names = ['Петя','Вова','леля']
names = list(map(lambda x: x.upper(),names))
print(names)

spisok = list(range(10,20))
print(spisok)
print(len(spisok)//3+1)
srez= len(spisok)//3+1
row = 1
a = 0
while row<=srez:
    print(spisok[a:a+3])
    row+=1
    a+=1

'''open, read, close, write
'''
'''r - для чтения
w - для записи
а - для добавления
r+ w+ a+ 
'''
file = open('123.txt', 'r',encoding='utf-8')
print(file)
r = file.read()
print(r)
file.close()

print('####################################')

file = open('123.txt', 'r',encoding='utf-8')
print(file)
r = file.readline()
print(r)
file.close()

print('####################################')

file = open('123.txt', 'r', encoding='utf-8')
file2 = open('456.txt', 'w', encoding='utf-8')

r = file.read()
file2.write(r)
file.close()
file2.close()

# a = input('name')
# b = input('film')
# c = input('eda')
# file66 = open('66.txt','w', encoding='utf-8')
# text = 'name '+ a +' \n' + 'film ' + b + ' \n' + 'eda ' + c + ' \n'
# file66.write(text)
# file66.close()

file = open('123.txt', 'r', encoding='utf-8')
spisok = []
for line in file:
    a=line.find('#')
    srez = line[a+1:-1]
    spisok.append(srez)


file.close()
print(*spisok,sep='\n')

# file11 = open('bob.txt', 'r', encoding='utf-8')
# file12 = open('bob2.txt', 'w', encoding='utf-8')
# text = file11.read()
# text1 = text.replace('боб','вова')
# file12.write(text1)
# file11.close()
# file12.close()

file11 = open('bob.txt', 'r', encoding='utf-8')
file12 = open('bob2.txt', 'w', encoding='utf-8')
file13 = open('info.txt', 'r', encoding='utf-8')

old = file13.readline().replace('\n','')
new = file13.readline().replace('\n','')
print(old,new)
file13.close()

text = file11.read()
text1 = text.replace(old,new)
file12.write(text1)
file11.close()
file12.close()