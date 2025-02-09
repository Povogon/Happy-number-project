import math

open("Results.txt","w").write("")
g = input("What's your number?")
target_sysg = 4 #int(input("What's your system(<=10)?")) uncomment the code for more choice
results = []

def convert(inp, target_sys): # for converting an input into a system 3(10) ==> 11(binary), kinda works for 10+ systems, but not really
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

def happy_check(n, target_sys):
    counter = 0
    log = []
    n = number(convert(n, target_sys))
    temp = [int(temp) for temp in str(n)]
    log.append("%s"%n)
    while True:
        i = 0
        temp = [int(temp) for temp in str(n)]
        while i < len(temp):
            temp[i] = temp[i] ** 2
            i = i + 1
        n = sum(temp)
        n = number(convert(n, target_sys))
        counter += 1
        log.append(">|%s|"%n)
        if n == 1:
            if counter >= 8:
                log.append("|    H%s    |" % counter)
            else:
                log.append("H%s  " %counter)
                return log

for j in range(int(g)):
    for k in happy_check(j+1, target_sysg):
        open("Results.txt", "a").write("%s" % k)
    #results.append(happy_check(j+1, target_sysg))
    #print(j)

for k in results:
    open("Results.txt","a").write("%s" %k)
print(results)