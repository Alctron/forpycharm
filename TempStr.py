N=input()
t=""
for i in N:
    if (ord(i)>=ord('A'))and(ord(i)<=ord('Z')):
        t=chr(ord('Z')-ord(i)+ord('A'))
    elif (ord(i)>=ord('a'))and(ord(i)<=ord('z')):
        t=chr(ord('z')-ord(i)+ord('a'))
    else:
        t=i
    print(t,end='')