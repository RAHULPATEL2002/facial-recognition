from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # upside First Image
        img = Image.open(r"D:\iiit surat\Facial Recognigation System\Collage_Images\student_upside_left.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)


        # upside Second Image
        img1 = Image.open(r"D:\iiit surat\Facial Recognigation System\Collage_Images\student_upside_middle.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)


        # upside Third Image
        img2 = Image.open(r"D:\iiit surat\Facial Recognigation System\Collage_Images\student_upside_right.jpg")
        img2 = img2.resize((550, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)


         # BackGroung Image
        img3 = Image.open(r"D:\iiit surat\Facial Recognigation System\Collage_Images\bg.jpg")
        img3 = img3.resize((1540, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_image = Label(self.root, image=self.photoimg3)
        bg_image.place(x=0, y=130, width=1540, height=710)

        # Lebel Title
        title_lbl=Label(bg_image,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="red",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # FRAME
        main_frame=Frame(bg_image,bd=2)
        main_frame.place(x=5,y=55,width=1515,height=590)

        # LEFT LEBEL FRAME
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Detail",font=("times new romen",12,"bold"))
        Left_frame.place(x=70,y=10,width=660,height=580)

        img_left = Image.open(r"D:\iiit surat\Facial Recognigation System\Collage_Images\student_left_frame.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=5, width=640, height=130)

        # Current Course Information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("times new romen",12,"bold"))
        current_course_frame.place(x=5,y=135,width=640,height=120)

        # Department
        deep_lebel=Label(current_course_frame,text="Department",font=("times new romen",13,"bold"),bg="white")
        deep_lebel.grid(row=0,column=0,padx=10,sticky=W)

        deep_combo=ttk.Combobox(current_course_frame,font=("times new romen",13,"bold"),width=20,state="readonly")
        deep_combo["values"]=("Select Department","CSE","ECE")
        deep_combo.current(0)
        deep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course
        course_lebel=Label(current_course_frame,text="Course",font=("times new romen",13,"bold"),bg="white")
        course_lebel.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("times new romen",13,"bold"),width=20,state="readonly")
        course_combo["values"]=("Select Course","B.Tech","M.Tech","B.Arch","MBA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        # Year
        year_lebel=Label(current_course_frame,text="year",font=("times new romen",13,"bold"),bg="white")
        year_lebel.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,font=("times new romen",13,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","1st","2nd","3rd","4th")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        # Year
        semester_lebel=Label(current_course_frame,text="Semester",font=("times new romen",13,"bold"),bg="white")
        semester_lebel.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,font=("times new romen",13,"bold"),width=20,state="readonly")
        semester_combo["values"]=("Select Semester","1","2","3","4","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        # Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Inforamtion",font=("times new romen",12,"bold"))
        class_student_frame.place(x=5,y=270,width=640,height=280)

        # Student Roll Number 
        StudentID_lebel=Label(class_student_frame,text="Roll No :",font=("times new romen",13,"bold"),bg="white")
        StudentID_lebel.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,font=("times new romen",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        # Student Name
        Student_name_lebel=Label(class_student_frame,text="Name :",font=("times new romen",13,"bold"),bg="white")
        Student_name_lebel.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,width=20,font=("times new romen",13,"bold"))
        student_name_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        # Student Gender
        gender_lebel=Label(class_student_frame,text="gender: ",font=("times new romen",13,"bold"),bg="white")
        gender_lebel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,font=("times new romen",13,"bold"),width=20,state="readonly")
        gender_combo["values"]=("Select gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        # Student DOB
        dob_lebel=Label(class_student_frame,text="DOB :",font=("times new romen",13,"bold"),bg="white")
        dob_lebel.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,width=20,font=("times new romen",13,"bold"))
        dob_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        # Student EMAIL ID
        email_lebel=Label(class_student_frame,text="Email :",font=("times new romen",13,"bold"),bg="white")
        email_lebel.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,width=20,font=("times new romen",13,"bold"))
        email_entry.grid(row=2,column=1,padx=2,pady=5,sticky=W)

        # Student PHONE NUMBER
        phone_lebel=Label(class_student_frame,text="Phone NO :",font=("times new romen",13,"bold"),bg="white")
        phone_lebel.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,width=20,font=("times new romen",13,"bold"))
        phone_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)

        # Student ADDRESS
        address_lebel=Label(class_student_frame,text="Address :",font=("times new romen",13,"bold"),bg="white")
        address_lebel.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,width=20,font=("times new romen",13,"bold"))
        address_entry.grid(row=3,column=1,padx=2,pady=5,sticky=W)

        # Student CGPA
        cgpa_lebel=Label(class_student_frame,text="CGPA :",font=("times new romen",13,"bold"),bg="white")
        cgpa_lebel.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        cgpa_entry=ttk.Entry(class_student_frame,width=20,font=("times new romen",13,"bold"))
        cgpa_entry.grid(row=3,column=3,padx=2,pady=5,sticky=W)


        # Radio Buttons
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,text="No Photo Sample",value="Yes")
        radiobtn2.grid(row=6,column=1)

        # Buttons  

        









        # RIGHT LEBEL FRAME
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Detail",font=("times new romen",12,"bold"))
        Right_frame.place(x=750,y=10,width=660,height=580)




if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
