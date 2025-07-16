x = int(input("x:"))
y = int(input("y:"))
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")


        # input: x -> print: odd/even

x = int(input("enter x: "))
if x%2 == 1:
    print("odd")
elif x%2 == 0:
    print("even")

       # input: x1, x2 -> print: quadratic equation without fraction

a= int(input("a: "))
b= int(input("b: "))
c= int(input("c: "))


term1 = -b
term2 = b**2- 4*a*c / 0.5
divisor = 2*a

x1 = term1 - term2 / divisor
x2 = term1 + term2 / divisor

print (x1, x2)

# input : 3 slides, a,b,c -> a+b>c, b+c>a, c+a>b; triangle

a= int(input("a: "))
b= int(input("b: "))
c= int(input("c: "))

if (a+b > c) and (b+c > a) and (c+a > b):
    print("it's a triangle")
else:
    print("it's not a triangle")

#if a+b>c:
#if b+c>a:
#if c+a>b:
#print("it's a triangle")

