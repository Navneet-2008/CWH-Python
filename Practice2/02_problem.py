l = ["abc","xyz","cbc","121"]
c = 0
for word in l:
    if(len(word) > 1) and (word[0] == word[-1]):
        c += 1
print(c)

