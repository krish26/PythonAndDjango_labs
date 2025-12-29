n=int(input())
lst=[]
for _ in range (n):
    cmd,*inputs=input().split()
    match cmd:
        case 'insert':  
            lst.insert(int(inputs[0]),int(inputs[1])) 
        case 'append':
            lst.append(int(inputs[0]))  
        case 'sort':
            lst.sort()
        case 'pop':
            lst.pop()   
        case 'reverse':
            lst.reverse()
        case 'remove':
            lst.remove(int(inputs[0]))
        case 'print':
            print(lst)              