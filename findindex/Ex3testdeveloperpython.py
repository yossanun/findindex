#ให้หา index ของตัวเลขที่มีค่ามากที่สุดใน Array

data = [1,2,1,3,5,6,4]
largest = data[0]
k = 0
for i in data:
    if i > largest:
        largest = i
    print('Loop:',i,largest)
print('Largest:',largest)

for j in data:
    if largest == j:
        break
    else:
        k = k + 1
print('Index:',k)