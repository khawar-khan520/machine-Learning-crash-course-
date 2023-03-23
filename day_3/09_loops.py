# while and for loops
# while loop
# x=0

# while (x<5):
#     print(x)
#     x= x+1

# for loops

# for x in range(5,10):
#     print(x)

days = ["mon","tue","wed","thur","fri","sat","sun"]

for d in days:
    # if (d=="fri"): break # breaks beforere d
    if (d=="fri"): continue 
    # it skips  d
    print(d)