pocket = int(input("enter a pocket number (0-36); "))

if pocket < 0 or pocket > 36:
    print("error: the pocket number must be between 0 and 36")
elif pocket == 0:
    print("green")
elif (1 <= pocket <= 10) or (19 <= pocket <= 28):
    print("red" if pocket % 2 == 1 else "black")
else:
    print("black" if pocket % 2 == 1 else "red")