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
    log = []
    counter = 0
    #print("Your number is %s" % n)
    #print("Log is %s" % log)
    temp = [int(temp) for temp in str(n)]
    #print("Temp is %s" % temp)
    while True:
        i = 0
        temp = [int(temp) for temp in str(n)]
        #print(log.count(n))
        if log.count(n) >= 1:
            #print("Loop found at n = %s" %n)
            #print("n index is %s" %log.index(n))
            return "L%s" %counter
        elif len(log) > 100:
            #print("no loop")
            return "N%s" %counter
        else:
            while i < len(temp):
                temp[i] = temp[i] ** 2
                i = i + 1
            n = sum(temp)
            if not(target_sys == 10):
                #print("%s into"%n)
                n = number(convert(n, target_sys))
                #print(n)
            log.append(n)
            counter += 1
        #print("Temp is %s" %temp)
        #print("Your number is %s" %n)
        #print("log is %s" %log)
        if n == 1:
            return "H%s" %counter

for j in range(int(g)):
    results.append(happy_check(j, target_sysg))
    #print(j)

for k in results:
    open("Results.txt","a").write("%s" %k)
print(results)