import csv,math,sys

class Thing:
  def __init__(self, i, d, l, t, c1, c2):
    self.id=i.upper()
    self.district=d.upper()
    self.location=l.upper()
    self.type=t.upper()
    self.lat=c1
    self.long=c2
  
  def __repr__(self):
    return "There's a {} {} in {}, {}, ({},{})".format(self.type, ("BBQ" if self.id[0]=="B" else ""), self.location, self.district, self.lat, self.long)

f=list(csv.reader(open("Drinking_Fountains.csv")))
b=list(csv.reader(open("Public_Barbeques_in_the_ACT.csv")))
t=list(csv.reader(open("Public_Toilets_in_the_ACT.csv")))

asc=open("art.txt").read().split("\n\n")

f=[Thing(x[0],x[1],x[2],"WATER FOUNTAIN",float(x[5]),float(x[6])) for x in f[1:]]
b=[Thing(x[0],x[1],x[2],x[3],float(x[5]),float(x[6])) for x in b[1:]]
t=[Thing(x[0],x[1],x[2],x[3],float(x[5]),float(x[6])) for x in t[1:]]

locs={x.location for x in f+b+t}-{""}
dists={x.district for x in f+b+t}

d={"TOILET":t,"LOO":t,"WATER":f,"DRINK":f,"FOUNTAIN":f,"WATER FOUNTAIN":f,"BBQ":b,"BARBEQUE":b}

#----------------------------------------------------------------

def near(l,w):
  return [x for x in d[w] if l in x.district]

def near5(c,w):
  c=[float(x) for x in c.strip("()").split(",")]
  return sorted(d[w],key=lambda x:dist(c[0],c[1],x.lat,x.long))[:5]

def iscoord(s):
  try:
    x,y=map(float,s.strip("()").split(","))
  except:
    return False
  return -90<=x<=90 and -180<=y<=180

def dist(x1,y1,x2,y2):
  dl=math.radians(y2-y1)
  df=math.radians(x2-x1)
  fm=math.radians(x1+x2)/2
  return 6371000*math.hypot(dl*math.cos(fm),df)

while True:
  print("\n"*5)
  print(asc[0])
  print("\n"*3)
  l=input(asc[1]+"\n").upper()
  while l not in locs|dists and not iscoord(l):
    print("Huh never heard of it. Try a REAL suburb or some proper coords.")
    l=input("So, where you at fam? ").upper()
  w=input("\n"*2+asc[2]+"\n").upper()

  if "MEME" in w:
    input("I warned you")
    input("This is my only one")
    try:
      print(asc[3])
    except:
      print("I lied I don't have any")
    w=input("Aight so whachu really after? ").upper()
  while w not in d:
    print("Huh whats dat? We only do bbq, toilet n water.")
    w=input("Aight so whachu really after? ").upper()

  if iscoord(l):
    n=near5(l,w)
  else:
    n=near(l,w)
    if 0<len(n)<5:
      n=near5(str((n[0].lat,n[0].long)),w)
  print("\n"*3)
  if n:
    print(asc[{"TOILET":4,"LOO":4,"WATER":5,"DRINK":5,"FOUNTAIN":5,"WATER FOUNTAIN":5,"BBQ":6,"BARBEQUE":6}[w]]+"\n"*3)
    print("Aight found some:")
    for i in n: print(i)
  else:
    print("Uh oh there's no "+w.lower()+" near you. Bad luck bro.")
  print("\n"*2)
  q=input("You good now? Or you want some more? (Y/N) ").upper()
  while q not in ("YESNO") or q[0] not in "YN":
    q=input("You good now? Or you want some more? (Y/N) ").upper()
  if q[0]=="N":
    break
  print("\n"*3)
