x = int(input("mantepse ton ari8mo"))
number = 0
pro = 0
while number != x and pro <=5 :
    if number > x:
        number = int(input(("dwse ari8mo mikrotero :")))
        pro += 1
    else:
        number = int(input(("dwse ari8mo megalutero :")))
        pro += 1
if number == x :
    print("to vrhkes!! einai to : " + str(number))
    print("ekanes" + str(pro) + "prospa8eies")
else:
    print("exases")