import random
state = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
jmlPopulasi = 16
def individu():
  pop = []
  for i in range(0,jmlPopulasi):
    pop.append([])
    for j in range(0,4):
      pop[i].append(random.choice(state))
  return pop
def crossover(a,b):
  pos = random.randrange(0,4)
  newa = b[:pos] + a[pos:]
  newb = a[:pos] + b[pos:]
  return newa,newb
def mutasi(s):
  pos = random.randrange(0,4)
  s[pos] = random.randrange(0,4)
  return s
def fitnes(s):
  fit = 0;
  for ic,i in enumerate(s):
    for jc,j in enumerate(s):
      if jc == ic:
        continue
      if j == i:
        fit += 5
      if j+1 == i:
        fit += 1
      if j-1 == i:
        fit += 1
      if j+3 == i:
        fit += 1
      if j-3 == i:
        fit += 1
      if j+4 == i:
        fit += 1
      if j-4 == i:
        fit += 1
      if j+5 == i:
        fit += 1
      if j-5 == i:
        fit += 1
  return fit
def init():
  popAwal = individu()
  generasi = -1
  while fitnes(popAwal[0]) != 0 and generasi < 100:
    generasi += 1
    popAwal =  sorted(popAwal, key=fitnes)
    elit = popAwal[:int(jmlPopulasi * 0.2)]
    hasil = elit
    while len(hasil) < jmlPopulasi:
      hasil.extend(crossover(random.choice(elit),random.choice(elit)))
    for i in range(0,len(hasil),int(len(hasil)/1)):
      hasil[i] = mutasi(hasil[i])
    popAwal =  sorted(hasil, key=fitnes)
  return popAwal[0]
def rekursif():
  x = init()
  if fitnes(x) != 0:
    x = rekursif()
  return x
tmp = []
for i in range(0,len(state)):
  tmp.append('0 ');
for i in rekursif():
  tmp[i] = 'R '
x = 'Hasilnya adalah :'
for i in range(0,len(state)):
  if i%4 == 0:
    x += '\n'
  x += tmp[i]
print x
