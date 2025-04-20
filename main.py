from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # upside First Image
        img = Image.open(r"D:\iiit surat\Facial Recognigation System\Collage_Images\upside_left.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)


        # upside Second Image
        img1 = Image.open(r"D:\iiit surat\Facial Recognigation System\Collage_Images\upside_middle.png")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)


        # upside Third Image
        img2 = Image.open(r"D:\iiit surat\Facial Recognigation System\Collage_Images\upside_right.jpg")
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
        title_lbl=Label(bg_image,text="FACE RECOGNITION SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Student Button
        img4 = Image.open(r"D:\iiit surat\Facial Recognigation System\Collage_Images\student_detail.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_image,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_image,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


        # Detect Face Button
        img5 = Image.open(r"D:\iiit surat\Facial Recognigation System\Collage_Images\face_detector.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2=Button(bg_image,image=self.photoimg5,cursor="hand2")
        b2.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_image,text="Face Detctor",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)


        # Attendence Button
        img6 = Image.open(r"D:\iiit surat\Facial Recognigation System\Collage_Images\attendence.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2=Button(bg_image,image=self.photoimg6,cursor="hand2")
        b2.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_image,text="Attendence",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)



         # Help Face Button
        img7 = Image.open(r"D:\iiit surat\Facial Recognigation System\Collage_Images\help_desk.png")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b2=Button(bg_image,image=self.photoimg7,cursor="hand2")
        b2.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_image,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)



        # Train Face Button
        img8 = Image.open(r"D:\iiit surat\Facial Recognigation System\Collage_Images\Train_data.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b2=Button(bg_image,image=self.photoimg8,cursor="hand2")
        b2.place(x=200,y=350,width=220,height=220)

        b1_1=Button(bg_image,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=550,width=220,height=40)


        # Photos Face Button
        img9 = Image.open(r"D:\iiit surat\Facial Recognigation System\Collage_Images\photos.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b2=Button(bg_image,image=self.photoimg9,cursor="hand2")
        b2.place(x=500,y=350,width=220,height=220)

        b1_1=Button(bg_image,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=550,width=220,height=40)



        # Developer Face Button
        img10 = Image.open(r"D:\iiit surat\Facial Recognigation System\Collage_Images\developer.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b2=Button(bg_image,image=self.photoimg10,cursor="hand2")
        b2.place(x=800,y=350,width=220,height=220)

        b1_1=Button(bg_image,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=550,width=220,height=40)


        # Exit Face Button
        img11 = Image.open(r"D:\iiit surat\Facial Recognigation System\Collage_Images\exit.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b2=Button(bg_image,image=self.photoimg11,cursor="hand2")
        b2.place(x=1100,y=350,width=220,height=220)

        b1_1=Button(bg_image,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=550,width=220,height=40)







if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
