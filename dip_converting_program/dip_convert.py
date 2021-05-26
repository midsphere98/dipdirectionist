dips = int(input("insert your dip value : "))
directions = int(input("insert your dip direction value : "))

direc = (directions - 90)
direc_after = (360-(directions + 90))


if directions < 90:                 ## north-east
    print("N",abs(direc),"W","/",dips,"NE")
elif 90<directions<180:             ## South-east
    print("N",direc,"E","/",dips,"SE")
elif 180<directions<270:            ## South-west
    print("N",direc_after,"W","/",dips,"SW")
elif 270<directions<360:            ## North-west
    print("N",abs(direc_after),"E","/",dips,"NW")
else:
    print("Check your value and fuck you")