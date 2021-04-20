tainies = ["tainia1", "tainia2", "tainia3", "tainia4"]

favorite = input("pes agaphmenh tainia")

if favorite in tainies :
    print("den egine apo8hkeush")
elif favorite not in tainies :
    tainies.append(favorite)
    tainies.sort()
    print(tainies)
    print(len(tainies))