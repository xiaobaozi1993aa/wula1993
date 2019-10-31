
a = input('输入url：')
number = a.count('=')
b = a.split('?')[1]
url = a.split('?')[0]
print(url)
c = b.split('&')
e = []
data = {}
for i in range(number):
    d = c[i].split('=')
    e.append(d)
for i in e:
    data[i[0]] = i[1]
print(data)

