my_list = [1, 10, 3]

cnt = 0
max=0
while cnt < len(my_list):
    if my_list[cnt] > max :
        max = my_list[cnt]
    cnt +=1
print(max)