# creating  a file 

# import os

# if not os.path.exists("student.txt"):
#     f = open("student.txt", "w")
#     f.close()
#     print("student.txt file created")
# else:
#     print("File already exists")



# write student data 

# f = open("student.txt", "a")

# roll = input("Enter Roll No: ")
# name = input("Enter Name: ")

# f.write(roll + "," + name + "\n")
# f.close()

# print("Student data saved")


#read student data

# f = open("student.txt", "r")

# print("Student Records:\n")
# print(f.read())

# f.close()

# # delete a file 

# import os

# if os.path.exists("student.txt"):
#     os.remove("student.txt")
#     print("student.txt deleted")
# else:
#     print("File not found")
