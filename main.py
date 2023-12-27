import random
import mysql.connector
import math

def initialise100(sub, prof, room, days, slots, n, qq):
    rows=days
    cols=slots
    
def initialise1(sub, prof, room, days, slots, n, qq):
    rows=days
    cols=slots
    dict={}
    list=[]
    subjects=[]
    for i in info[n]:
        dict[i]=[sub[i][0], sub[i][1]]
        subjects.append(i)


    sum=0
    for i in dict:
        sum+=dict[i][0]*dict[i][1]
    if(sum>rows*cols):
        print("Invalid input. Not enough slots available")

    i=0
    while i<rows:
        random.shuffle(subjects)
        col=[0]*cols
        k=0
        j=0
        while(j<cols and k<len(subjects)):
            if dict[subjects[k]][0]>0:
                if (cols - j) >= dict[subjects[k]][1]:
                    dict[subjects[k]][0]-=1
                    for f in range(dict[subjects[k]][1]):
                        col[j]=subjects[k]
                        j+=1
                k+=1
            else:
                k+=1
        if qq==True:
            col.reverse()
            qq=False
        else:
            qq=True
        list.append(col)
        i+=1
    sum1=0
    for i in range(rows):
        for j in range(cols):
            if list[i][j]!=0:
                sum1+=1
    if(sum1<sum):
        return initialise(sub, prof, room, days, slots, n, qq)
    else:
        list.reverse()
        return list

def initialise(sub, prof, room, days, slots, n, qq):
    rows=days
    cols=slots
    dict={}
    list=[]
    subjects=[]
    for i in info[n]:
        dict[i]=[sub[i][0], sub[i][1]]
        subjects.append(i)


    sum=0
    for i in dict:
        sum+=dict[i][0]*dict[i][1]
    if(sum>rows*cols):
        print("Invalid input. Not enough slots available")

    i=0
    while i<rows:
        random.shuffle(subjects)
        col=[0]*cols
        k=0
        j=0
        while(j<cols and k<len(subjects)):
            if dict[subjects[k]][0]>0:
                if (cols - j) >= dict[subjects[k]][1]:
                    dict[subjects[k]][0]-=1
                    for f in range(dict[subjects[k]][1]):
                        col[j]=subjects[k]
                        j+=1
                k+=1
            else:
                k+=1
        if qq==False:
            col.reverse()
            qq=True
        else:
            qq=False
        list.append(col)
        i+=1
    sum1=0
    for i in range(rows):
        for j in range(cols):
            if list[i][j]!=0:
                sum1+=1
    if(sum1<sum):
        return initialise(sub, prof, room, days, slots, n, qq)
    else:
        return list




def fitness(sub, prof, room, days, slots, list):
    conflict=0
    proof={}
    for i in range(days):
        for j in range(slots):
            for k in list:
                if list[k][i][j]!=0:
                    if info[k][list[k][i][j]] in proof:
                        conflict+=1
                if(list[k][i][j]!=0):
                    proof[info[k][list[k][i][j]]]=True
            proof.clear()
    return conflict



def mutation(list, v):
    if(v>=1):
        return

    i=random.randint(0, len(list)-1)
    if i==len(list):
        i-=1
    j=random.randint(0, len(list[0])-1)
    if j==len(list[0]):
        j-=1
    i1=random.randint(0, len(list)-1)
    if i1==len(list):
        i1-=1
    j1=random.randint(0, len(list[0])-1)
    if j1==len(list[0]):
        j1-=1
    if (i==i1 and j==j1) or (list[i][j]==list[i1][j1]) or (list[i][j]==0 and list[i1][j1]==0) or list[i][j]==0:
        mutation(list, v)
        return

    while j>0 and list[i][j-1]==list[i][j]:
        j=j-1
    if list[i1][j1]!=0:
        while j1>0 and list[i1][j1-1]==list[i1][j1]:
            j1=j1-1
    else:
        count=sub[list[i][j]][1]-1
        while(len(list)-1-j1<count) and j1>0:
            j1-=1
    if (j>0 and list[i][j-1]==list[i1][j1]) or (j1>0 and list[i1][j1-1]==list[i][j]):
        mutation(list, v)
        return
    count1, count2=(0,0)
    a, b, a1, b1=(i, j, i1, j1)
    count=sub[list[i][j]][1]-1
    while b<len(list[0])-1 and count>0:
        count1+=1
        b+=1
        count-=1

    while count2<count1 and b1<len(list[0])-1:
        count2+=1
        b1+=1
    if b1<len(list[0])-1 and list[a1][b1]==list[a1][b1+1]:
        mutation(list, v)
        return
    if (j<len(list)-2 and list[i][j+1]==list[i1][j1]) or (j1<len(list)-2 and list[i1][j1+1]==list[i][j]):
        mutation(list, v)
        return
    if count1!=count2:
        mutation(list, v)
        return
    while j<=b and j1<=b1:
        temp=list[i][j]
        list[i][j]=list[i1][j1]
        list[i1][j1]=temp
        j+=1
        j1+=1
    mutation(list, v+1)



def crossover(list1, list2, f, n, mini, f1, f2, v):

    list3={}
    list4={}

    k=0
    for i in list1:
        if k<f:
            list3[i]=list1[i]
            k+=1
        else:
            break

    k=0
    for i in list2:
        if k<f:
            list4[i]=list2[i]
            k+=1
        else:
            break

    for i in list3:
        list2[i]=list3[i]

    for i in list4:
        list1[i]=list4[i]

    c=random.randint(0, len(cl)-1)
    while cl[c] not in info:
        c = random.randint(0, len(cl) - 1)
    mutation(list1[cl[c]], 0)

    c=random.randint(0, len(cl)-1)
    while cl[c] not in info:
        c = random.randint(0, len(cl) - 1)
    mutation(list2[cl[c]], 0)

    main1[v]=list1
    main1[v+1005]=list2


mydb = mysql.connector.connect(host="localhost", user="root", password="hardwell123", database="tt")
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM sub")
myresult = mycursor.fetchall()
sub={}
for row in myresult:
    sub[row[0]]=[row[1], row[2]]

mycursor.execute("SELECT * FROM prof")
myresult = mycursor.fetchall()
prof={}
for row in myresult:
    prof[row[0]]=True


mycursor.execute("SELECT * FROM room")
myresult = mycursor.fetchall()
room={}
cl=[]
for row in myresult:
    room[row[0]]=True
    cl.append(row[0])


mycursor.execute("SELECT * FROM info")
myresult = mycursor.fetchall()
info={}
for row in myresult:
    info[row[0]]={}
for row in myresult:
    info[row[0]][row[1]]=row[2]

mycursor.execute("SELECT * FROM no_of_days")
myresult = mycursor.fetchall()

for row in myresult:
    days=row[0]


mycursor.execute("SELECT * FROM no_of_slots")
myresult = mycursor.fetchall()

for row in myresult:
    slots=row[0]




mainlist={}
for i in range(1000):
    mainlist[i]={}
    qq=False
    akk=True
    for j in room:
        if j not in info:
            continue
        if akk==True:
            list=initialise(sub, prof, room, days, slots, j, qq)
            akk=False
        else:
            list=initialise1(sub, prof , room, days, slots, j, qq)
            akk=True
        mainlist[i][j]=list



main=[]
for i in mainlist:
    main.append([fitness(sub, prof, room, days, slots, mainlist[i]), mainlist[i]])
main.sort(key=lambda x: x[0])


print(main[0][0])
print(main[len(main)-1][0])
for i in main[0][1]:
    print(main[0][1][i])
k=1
main1={}
while main[0][0]!=0:
    print(main[0][0])
    print(main[len(main)-1][0])
    k+=1
    main1={}

    mini = main[0][0]

    mainl = []
    if len(main)==2:
        for i in range(2):
            mainl.append([main[i][0], main[i][1]])
    else:
        for i in range(40):
            mainl.append([main[i][0], main[i][1]])

    for i in range(30):
        main1[i]={}
        main1[i+1005]={}
        f = random.randint(0, len(main[0][1])-1)
        while f == 0:
            f = random.randint(0, len(main[0][1]))
        a = random.randint(0, len(main) - 1)

        b = random.randint(0, len(main) - 1)
        while b == a:
            b = random.randint(0, len(main) - 1)

        list1=main[a][1].copy()
        list2=main[b][1].copy()
        f1=main[a][0]
        f2=main[b][0]
        crossover(list1, list2, f, 0, mini, f1, f2, i)

    main.clear()
    for i in range(len(mainl)):
        main.append([mainl[i][0], mainl[i][1]])
    for i in main1:
        main.append([fitness(sub, prof, room, days, slots, main1[i]), main1[i]])

    main.sort(key=lambda x: x[0])

print(main[0][0])
for i in main[0][1]:
    print(main[0][1][i])
print(len(main))
print(k)


