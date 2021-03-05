from time import time
t=time()
print(t)
#z=(ctime(t))
#print(z)
print('write your name down here')
k=input()
#s=[k]
import random
count=0
for i in range(10):
    list=[1,2,3,4,]
    #count=[]
    c=random.choice(list)
    print('pick a number from 1 to 4')
    print('YOU PICKED LUCKY NUMBER')
    z=input()
    print(c)
    #z=input()
    #for i in range(10):
    if int(z)==int(c):
        count+=1
        #print(count)
        print('I THINK U ARE LUCKY;)')
    else:
        count+=0
        print('TRY NEXT TIME:(')
if count<=3:
    print('YOU CAN DO IT BETTER and YOUR SCORE IS')
else:
    print('AWESOME:)')
print('YOUR TOTAL SCORE IS')
z=[count]
d=[]
#z.append(d)
print(z)

#z.append(d)
j=(k,count,t)
print(j)

with open('listfile.txt', 'a') as filehandle:
    #filecontents=filehandle.write()
    for listitem in j:
        filehandle.write('%s\n' % listitem)
    #filehandle.read()
    f = open('listfile.txt', 'r')
    leaderboard = [line.replace('\n', '') for line in f.readlines()]
    for i in leaderboard:
        print(i)
# list=open('listfile.txt').read().splitlines()
# print(list)
# done=open('leaderboard','w')
# done.append(z)
# print(done)

with open('listfile.txt', 'r') as f:
    t = f.readlines()
    i = 0
    num_users = len(t)/3
    print(num_users)
    all_users = []
    for user in range(int(num_users)):
        u =[]
        u.sort()
        for x in range(3):
            u.append(t[i+x])
        i+=3
        all_users.append(u)
    #print(all_users)
def Sort(all_users):
    all_users.sort(key=lambda x:x[1],reverse=True)
    return all_users
z=(Sort(all_users))
print(z)
print(k,'your rank is')
print(z.index(u)+1)






















