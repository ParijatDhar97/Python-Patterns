n= int(input())
d=0
c=0
count=0
loop=(n*n)
dec=n*2-1
space=0

for i in range(1,n+1):
    # for dashes
  def dashprint():
    for j in range(1,d+1):
      print('-', end='')
  
  # for left right angle traingle with *
 
  for k in range(1,(n*2-d)+1):
      if k==1:
        dashprint()
      if k%2==0:
          print(end='*')
      else:
          c=c+1
          print(c,end='')
          
  # for left right angle traingle with *

  for r in range(1,((n*2)-space)):
    if r%2==0:
      print(end='*')
    else:
      loop=loop+1
      print(loop,end='')
  
  loop=loop-dec
  dec=dec-2
  space+=2
  d=d+2
  print()

#   1*2*3*4*17*18*19*20
# --5*6*7*14*15*16
# ----8*9*12*13
# ------10*11