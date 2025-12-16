#Coding Challenge 43: Whole and Fraction value separation
# import math
n=float(input("Enteer double value:"))
# whole=int(n)
# fraction=n-whole
#fraction,whole=math.modf(n)
n=str(n)
if '.' in n:
    whole,fraction=n.split('.')
    print("whole part:",whole)
    print(f"fraction part 0.{fraction}")
else:
    print("whole part:",n)
    print("fraction part",0)