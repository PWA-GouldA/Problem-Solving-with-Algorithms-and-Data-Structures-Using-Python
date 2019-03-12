def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + (pos+1) * ord(astring[pos])

    return sum%tablesize

print(hash('hashing', 11))
print(hash('hushing', 11))