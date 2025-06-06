from tkinter import*
from PIL import Image,ImageTk  
from course import CourseClass
from student import StudentClass
from result import resultclass
from report import reportclass
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("SRMS")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #===icons===
        self.logo_dash=ImageTk.PhotoImage(file="images/logo_j.jpg")

        #===title===
        title=Label(self.root,text="STUDENT RESULT MANAGEMENT SYSTEM",padx=10, compound= LEFT , image=self.logo_dash, font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)

        #===menu=====
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1500,height=80)

        #===content_window===
        self.bg_img=Image.open("images/bg.jpg")
        self.bg_img=self.bg_img.resize((950,350),Image.Resampling.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=1000,height=430)

        #===update_details===
        
        self.lbl_course=Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=20,relief=RIDGE,bg='#e43b06',fg="white")
        self.lbl_course.place(x=440,y=620,width=300,height=100)

        self.lbl_student=Label(self.root,text="Total Students\n[0]",font=("goudy old style",20),bd=20,relief=RIDGE,bg='#e43b06',fg="white")
        self.lbl_student.place(x=750,y=620,width=300,height=100)

        self.lbl_result=Label(self.root,text="Total Results\n[0]",font=("goudy old style",20),bd=20,relief=RIDGE,bg='#e43b06',fg="white")
        self.lbl_result.place(x=1070,y=620,width=300,height=100)


        
        #===button===
        btn_course=Button(M_Frame,text="COURSES",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=60,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="STUDENTS",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=360,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="RESULT",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=720,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="VIEW RESULT",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=1080,y=5,width=200,height=40)
        
        #===FOOTER===
        footer=Label(self.root,text="SRMS-STUDENT RESULT MANAGEMENT SYSTEM", font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=X)

    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=StudentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultclass(self.new_win)


    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportclass(self.new_win)

    




if __name__=="__main__":
    root=Tk() 
    obj=RMS(root)
    root.mainloop()        