import re

f = open("string_data","r")
arr=[]
tsr = f.readlines()
#print(len(tsr.replace(' ',''))

for line in tsr:
  tmp=re.search(r'".{5,10}"',line.replace(' ',''))
#.replace(' ',''))
  if tmp!=None:
    #print(tmp)
    #print(tmp.group())
    ll=line.replace(' ','')
    print(ll[tmp.start()+1:tmp.end()-1])
    arr.append(ll)
print(len(arr))
