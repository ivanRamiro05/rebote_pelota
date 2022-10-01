#input
H=int(input("ingrese la altura desde la cual desea lanzar la pelota: "))
i=0
B=H
#processing
while B > H*0.2:
    i=i+1
    B=B - B*0.1
print(i)
