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
while j<5:
  x=random.randint(1,50)
  if unico(x,L):
    L.append(x)
    j+=1
L.sort()
print(L)
L=[]
j=0
while j<2:
  x=random.randint(1,12)
  if unico(x,L):
    L.append(x)
    j+=1
print(L)