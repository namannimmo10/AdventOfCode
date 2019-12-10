
arr = [int(i) for i in open("Day2-input").read().split(",")]
arr[1],arr[2] = 12,2

for _ in range(0,len(arr),4):
    opcode = arr[_]
    a1 = arr[_+1]
    a2 = arr[_+2]
    a3 = arr[_+3]

    if opcode==1:
        arr[a3]=arr[a2]+arr[a1]
    elif opcode==2:
        arr[a3]=arr[a2]*arr[a1]
    else:
        break
print(arr[0])
