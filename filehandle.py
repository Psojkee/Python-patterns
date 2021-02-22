fname = input('filename')
x=open(fname)
count=0
avg=0
for line in x:
    if line.startswith('X-DSPAM-Confidence:'):
        count=count+1
        avg=avg+float(line[20:27])
    else:
        continue
av=avg/count
print('Average spam confidence:', av)
