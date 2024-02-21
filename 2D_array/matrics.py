array1 = [[1,2],
          [3,4],
          [4,5]]
#print(array1[2][1])

for obj in array1:
    for ele in obj:
        print(ele, end=",")
    print()

for obj in  range(5):
    for ele in range(3):
        print(f'[{obj} {ele}]')