dic={"Alice":89,"Bob":90,"John":87,"Ram":98}
data=input("Enter the student name : ")
while True:
    if data in dic :
        print(dic[data])
        break
    else :
        print("Student Not Found")
        break