import math
log = []
temp = []
i = 0
n = input("What's your number?")
target_sys = int(input("What's your system(<=10)?"))

def convert(inp, target_sys): # for converting an input into a system, kinda works for 10+ systems, but not really
    i = True
    out = []
    while i:
        quo = math.floor(inp / target_sys)
        if quo < 1:
            i = False
        out.insert(0, inp % target_sys)
        inp = quo
    return out

def number(input): #converts list to a number [1,2,3] ==> 123
    value = 0
    for m in range(len(input)):
        if not(m>len(input)):
            value += input[m]*(10**(len(input) - m-1))
    return value


print("Your number is %s" %n)
print("Log is %s" %log)
temp = [int(temp) for temp in str(n)]
print("Temp is %s" %temp)
while True:
    if log.count(n) > 1:
        print("Loop found at n = %s" %n)
        print("n index is %s" %log.index(n))
        break
    elif len(log) > 100:
        print("no loop")
        break
    else:
        while i < len(temp):
            temp[i] = temp[i] ** 2
            i = i + 1
        n = sum(temp)
        if not(target_sys == 10):
            n = number(convert(n, target_sys))
        log.append(n)
    print("Temp is %s" %temp)
    print("Your number is %s" %n)
    i = 0
    temp = [int(temp) for temp in str(n)]
    

print("End of line")
print("Temp is %s" %temp)
n = sum(temp)
print("Your number is %s" %n)
print("Log is %s" %log)
if n == 1:
    print("Happy number!!!")