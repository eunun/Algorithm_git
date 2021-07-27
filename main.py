#8979번 올림픽
N, K = map(int, input().split())
medallist = []
num = []
gold = []
silver = []
bronze = []
for n in range(N):
  a, b, c, d = map(int, input().split())
  num.append(a)
  gold.append(b)
  silver.append(c)
  bronze.append(d)
  if num[n] == K:
    key = n
for i in range(len(num)):
  if i==key:
    continue
  if gold[i]>gold[key]:
    medallist.append(num[i])
  elif gold[i]==gold[key]:
    if silver[i]>silver[key]:
      medallist.append(num[i])
    elif silver[i]==silver[key]:
      if bronze[i]>bronze[key]:
        medallist.append(num[i])
print(len(medallist)+1)