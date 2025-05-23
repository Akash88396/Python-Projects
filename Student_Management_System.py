import mysql.connector as mc

#database connection

link = mc.connect(host="localhost",user="root",password="Akash@k47",database="Student_Management")

student_mg = link.cursor()

# make function to add student in database

def add_student():
    name =input("Enter Student Name :")
    grade =input("Enter Class :")
    Dob = input("Enter D.O.B (YYYY-MM-DD) :")
    phone=input("Enter  Contact Number:")
    email= input("Enter Email:")
    address = input("Enter Address :")
    gender = input("Enter Gender (M/F):")

    student_mg.execute("insert into student_data(name,grade,email,phone,address,gender,dob) values (%s,%s,%s,%s,%s,%s,%s)",(name,grade,email,phone,address,gender,Dob))

    link.commit()

    print("Added Successfully!!")

# make function to   show all students details

def show_students_info():
    student_mg.execute("Select * from student_data")

    for(RollNumber,name,grade,email,phone,address,gender,dob) in student_mg.fetchall():
        print(f"RollNumber:{RollNumber}\nName:{name}\nGrade:{grade}\nEmail:{email}\nPhone:{phone}\nAddress:{address}\nGender:{gender}\nD.O.B:{dob}\n")
        
# make fuction to search student in database
      
def search_student():
    student_rollNumber =int(input("Enter student Roll number:"))
    student_mg.execute("select * from student_data where Roll_number =%s",(student_rollNumber,))

    result =student_mg.fetchone()

    if result:
        
            print(f"RollNumber:{result[0]} ,Name:{result[1]},Grade:{result[2]},Email:{result[3]},Phone:{result[4]},Address:{result[5]},Gender:{result[6]},D.O.B:{result[7]}")
            
    else:
        print("Student not found.")


def update_student():

    student_id = int(input("Enter student ID to update: "))

    choice = input("What you want to update:\nSelect one (Name,Grade,Email,Phone,Address,Gender,D.O.B,All)\n->").lower().strip()

    if choice == "name":
         newName=input("Enter new name:")
         student_mg.execute("update student_data set name=%s where roll_number=%s",(newName,student_id))

         link.commit()
         print("Name is updated!")

    elif choice == "grade":
         newGrade=input("Enter new Grade:")
         student_mg.execute("update student_data set grade=%s where roll_number=%s",(newGrade,student_id))

         link.commit()
         print("Grade is updated!")

    elif choice == "email":
         newEmail=input("Enter new Email:")
         student_mg.execute("update student_data set email=%s where roll_number=%s",(newEmail,student_id))

         link.commit()
         print("Email is updated!") 

    elif choice == "phone":
         newphone=input("Enter new Contact number:")
         student_mg.execute("update student_data set phone=%s where roll_number=%s",(newphone,student_id))

         link.commit()
         print("Phone is updated!")   

    elif choice == "address":
         newAddress=input("Enter new Address:")
         student_mg.execute("update student_data set address=%s where roll_number=%s",(newAddress,student_id))

         link.commit()
         print("Address is updated!")         

    elif choice == "gender":
         newGender=input("Enter new Gender:")
         student_mg.execute("update student_data set gender=%s where roll_number=%s",(newGender,student_id))

         link.commit()
         print("Gender is updated!")    

    elif choice == "dob":
         newdob=input("Enter new D.O.B:")
         student_mg.execute("update student_data set dob=%s where roll_number=%s",(newdob,student_id))

         link.commit()
         print("DOB is updated!")    

    elif choice == "all":
         newName=input("Enter new Name:")
         newGrade=input("Enter new Grade:")
         newEmail=input("Enter new Email:")
         newphone=input("Enter new Contac number:")
         newAddress=input("Enter new Address:")
         newGender=input("Enter new Gender:")
         newdob=input("Enter new DOB:")

         student_mg.execute("update student_data set name=%s,grade=%s,email=%s,phone=%s,address=%s,gender=%s,dob=%s where roll_number=%s",(newName,newGrade,newEmail,newphone,newAddress,newGender,newdob,student_id))

         link.commit()
         print("Student details is updated!") 

    else:
         print("Invalid choice!")       


def delete_student():
     
     student_id = input("Enter Student Roll number:")

     student_mg.execute("SELECT * FROM student_data WHERE roll_number = %s", (student_id,))

     result = student_mg.fetchone()

     if result:
          student_mg.execute("delete from student_data where roll_number =%s",(student_id,))
          link.commit()
          print("Student deleted successfully!")

          
     else:
          print("Student not found!")



while True:
     print("----STUDENT MANAGEMENT SYSTEM----")
     choice =input("Select one:\n1.Add Student\n2.Show Students\n3.Search Student\n4.Update Student Details\n5.Delete Student\n6.Exit\n->")

     match choice:
          case '1':
               add_student()
          case '2':
               show_students_info()
          case '3':
               search_student()   
          case '4':
               update_student()
          case '5':
               delete_student()
          case '6': 
               print("👋 Exiting... Goodbye!")
               break   
          case _:
               print("Invalid choice! Please try again..")               

         
    
