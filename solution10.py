#Coding Challenge 10: Student Report Card Problem 
name=input("Enter your name:")

def get_marks(subject):
    marks_input=input(f"Enter marks for {subject}:" )

    temp=marks_input.replace('-','',1)

    if not temp.replace(".","",1).isdigit():
        print(f"Invalid marks enterd for {subject}")
        exit()
    
    marks=float(marks_input)

    if(marks<0 or marks>100):
        print(f"Marks must be between 0 and 100 for {subject}")
        exit()
    
    return marks

sub1=get_marks("subject1")
sub2=get_marks("subject2")
sub3=get_marks("subject3")
total=sub1+sub2+sub3
average=total/3
if(average>=60):
    print(f"{name}\ntotal:{total}\naverage:{average}\nsecured:1st Class")
elif(average>=50):
    print(f"{name}\ntotal:{total}\naverage:{average}\nsecured:2nd Class")
elif(average>=35):
    print(f"{name}\ntotal:{total}\naverage:{average}\nsecured:Pass Class")
else:
    print(f"{name}\ntotal:{total}\naverage:{average}\nsecured:Fail")
