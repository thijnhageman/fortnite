
out = open("nummers.txt", "w")
mssg = "![{}](pics/{}.jpg)"

for i in range(251, 1000):
    print(mssg.format(i, i), file=out)
    print(file=out)
out.close()
print("klaar")