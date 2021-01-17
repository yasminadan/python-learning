text = input("Input any text: ")

print(text.strip())


print(len(text))

print(text.upper())

print(text[::3])
text[2:3] = "b"

def addTwo(x):
    return x + 2

newNumber = addTwo(5)
print(newNumber)    

def accel(mass, force):
    a = mass * force
    return a

accel_number = accel(int(4), int(7))
print(accel_number) 