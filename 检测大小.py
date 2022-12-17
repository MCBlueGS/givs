import os
yesc=0
noc=0
fl=os.listdir()
for i in fl:
    a=str(os.stat(i))
    a=a.split(', ')
    qw=''
    for i in a:
        if 'st_size=' in i:
            qw=int(i.strip('st_size='))
    if qw/1024/1024<=25:
        yesc=yesc+1
    else:
        noc=noc+1
print('小于25MB的:'+str(yesc))
print('大于25MB的:{}'.format(noc))
print('通过概率：{}%'.format(round(yesc/(yesc+noc)*100,2)))
os.system('pause')
