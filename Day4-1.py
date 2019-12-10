

#################################
res= 0

for x in range(206938,679129):
    dec_bool, double_bool = False, False
    string = str(x)
    for i in range(len(string)-1):
        if int(string[i])>int(string[i+1]):
            dec_bool = True
        elif int(string[i])==int(string[i+1]):
            double_bool = True
    if (double_bool == True) and (dec_bool == False):
        res += 1

print(res)
