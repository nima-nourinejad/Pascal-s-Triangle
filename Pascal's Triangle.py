def pt (a):
  out=[]
  line=[]
  s=a
  st='  '
  for i in range (a):
       if i==0:
        line.append(1)
       else:
         for j in range (i+1):
          if j==0:
           line.append(1)
          elif j!=i:
           t1=out[i-1][j-1]
           t2=out[i-1][j]
           line.append (t1+t2)
          elif j==i:
           line.append (1)
       out.append (line)
       print (s*st, end='' )
       s=s-1
       for i in line:
        print(i, end='' )
        print('  ', end='')
       print('\n')
       line=[]
