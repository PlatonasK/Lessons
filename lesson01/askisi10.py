hours = int(input("dwse wres :"))
min = int(input ("dwse lepta :"))
sec = int(input ("dwse deutera :"))

if hours < 10 :
    hours = ("0" + str(hours))
if min < 10 :
    min = ("0" + str(min))
if sec < 10 :
    sec = ("0" + str(sec))



print (str(hours) + ":" + str(min) + ":" + str(sec) )