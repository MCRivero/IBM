import random
def unico(x,L):
  esUnico=True
  for i in range(len(L)):
    if x==L[i]:
      esUnico=False
      break
  return esUnico
L=[]
j=0
while j<6:
  x=random.randint(1,49)
  if unico(x,L):
    L.append(x)
    j+=1
print(L)
L.sort()
print(L)
L=[]
j=0
while j<1:
  x=random.randint(1,9)
  if unico(x,L):
    L.append(x)
    j+=1
print(L)