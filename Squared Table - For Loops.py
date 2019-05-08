print("Numbers between 1 and 100 with their squared values")
print("___________________________________________________")

print("Numbers are printed alongside their squared value")
for x in range (1, 101):

    print ("%d: %d" % (x, x*x))


print("Applications stops when the squared value of 200 or more is reached")
print("___________________________________________________________________")

for x in range(1, 101):
    if x * x >= 200:
        break
    print("%d: %d" % (x, x * x))
print("Job Done!")
