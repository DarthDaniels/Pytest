skip = 0
for i in range(1, 100):
    if skip != 0:
        skip -= 1
        continue
    if ...... :
        #do stuff
    else:
        skip = 1
        #do other stuff