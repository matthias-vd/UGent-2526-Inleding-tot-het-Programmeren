i=0
gl=[]
a3=0
while i!=10:
    gl.append(int(input()))
    i+=1
for e in gl:
    if e%3==0:
        a3+=1
print(f'grootste: {max(gl)}')
print(f'kleinste: {min(gl)}')
print(f'drievouden: {a3}')