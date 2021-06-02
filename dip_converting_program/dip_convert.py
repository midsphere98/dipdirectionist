####this is a hard-coded dip direction convert program made with python.

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#prompt some hello message
print(color.BOLD + color.CYAN + """\n\n\n##############################################
##                                          ##
##             Dip-Directionist             ##
##           wrote by jungwon choi          ##
##                                          ##
##############################################
""" + color.END)

print(color.BOLD +"Introduction"+color.END)
print("\tyou aquired dip-dipdirection data from your field, right?")
print("\tnow all you need to do is insert data to terminal!\n")




dips = int(input(color.BOLD + "insert your dip value : " + color.GREEN ))
directions = int(input(color.END + color.BOLD + "insert your dip direction value : " + color.GREEN))
print(color.END)
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
    print("Check your value")
