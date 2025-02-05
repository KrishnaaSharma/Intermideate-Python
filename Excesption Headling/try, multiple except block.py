x = 10
y = 0

# z = x/y
# print(z)

try:
    z = x/y
    print(z)

except ZeroDivisionError:
    print("Error: Number Cannot be divide zero")

except NameError as k:
    print("Error {k}")

except SyntaxError as e:
    print("Error : {e}")







    
