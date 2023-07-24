# DemoIndexing.py

strA="Python is very powerful"
print(strA[0])
print(strA[1])
print(strA[0:3])
print(strA[:3])
print(strA[:])
print(strA[-3:])
print(strA[-8:])

colors=['red','blue','green']
print(colors)
print(len(colors))
print(colors[0])
colors.append('black')
print(colors)

for item in colors:
    print(item)
    
colors.append("white")
print(colors)
colors.insert(1,'pink')
print(colors)
print(colors.index('red'))
colors+='pink'
print(colors.pop())

print(colors)
colors.append('black')
print(colors)
colors.sort()
print(colors)