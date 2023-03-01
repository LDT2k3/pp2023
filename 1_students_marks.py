n=int(input("number of students in a class"))
stu_id=list()
stu_name=list()
stu_dob=list()
for i in range (n):
    j=input("ID of student "+str(i+1)+": ")
    stu_id.append(j)
    j=input("Name of student "+str(i+1)+": ")
    stu_name.append(j)
    j=input("Date of birth of student "+str(i+1)+": ")
    stu_dob.append(j)

m=int(input("Number of course: "))
course=dict()
cousre_name=list()
for i in range(m):
   course.setdefault(input("ID of course "),input("Name of course: "))

for i in course.values():
    cousre_name.append(i)    

marks=[]
for i in range(m):
    for j in range(n):
        k=float(input( cousre_name[i]+" score of "+stu_name[j]+": "))
        marks.append(k)

cnt=0

print("\n")
print("List of student:")
for i in range(n):
    print(stu_id[i],stu_name[i],stu_dob[i])
  
for i in range(m):
    for key, value in course.items():
        print(key, value)
    for j in range(n):
        print(stu_id[j],stu_name[j]+": ",marks[cnt])
        cnt+=1   