from tkinter import*
from PIL import Image,ImageTk  
from tkinter import ttk, messagebox
import sqlite3
class reportclass:
    def __init__(self,root):
        self.root=root
        self.root.title("SRMS")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #===title======================
        title=Label(self.root,text="VIEW STUDENT RESULT", font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=50)
        #======search=================
        self.var_search=StringVar()
        self.var_id=""

        lbl_search=Label(self.root,text="Search By Roll No.",font=("goudy old style",20,"bold"),bg="white").place(x=280,y=100)
        txt_search=Entry(self.root,textvariable=self.var_search,font=("goudy old style",20), bg="lightyellow").place(x=520,y=100,width=150)
        btn_search=Button(self.root,text="SEARCH",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=680,y=100,width=100,height=28)
        btn_clear=Button(self.root,text="CLEAR",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.clear).place(x=800,y=100,width=100,height=28)


        #=======result_labels===========
        lbl_roll=Label(self.root,text="Roll",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_coures=Label(self.root,text="Courses",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_marks_ob=Label(self.root,text="Marks obtained",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        lbl_full_marks=Label(self.root,text="Total Marks",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        lbl_per=Label(self.root,text="Percentage",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)

        self.roll=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.roll .place(x=150,y=280,width=150,height=50)
        self.name=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.coures=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.coures.place(x=450,y=280,width=150,height=50)
        self.marks_ob=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.marks_ob.place(x=600,y=280,width=150,height=50)
        self.full_marks=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.full_marks.place(x=750,y=280,width=150,height=50)
        self.per=Label(self.root,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE)
        self.per.place(x=900,y=280,width=150,height=50)

        #=======delete========
        btn_delete=Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.delete).place(x=500,y=350,width=150,height=35)
#===============================================================================================================

    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("error","roll.no is required",parent=self.root)
            else:
                cur.execute("select * from result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row != None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.coures.config(text=row[3])
                    self.marks_ob.config(text=row[4])
                    self.full_marks.config(text=row[5])
                    self.per.config(text=row[6])

                else:
                    messagebox.showerror("error","no record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("error",f"Error due to {str(ex)}") 

    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.coures.config(text="")
        self.marks_ob.config(text="")
        self.full_marks.config(text="")
        self.per.config(text="")
        self.var_search.set("")


    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search Student Result First",parent=self.root)
            else:
                cur.execute("select * from result where rid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Student Result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from result where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("delete","Result deleted successfully",parent=self.root)
                        self.clear()
        
        except Exception as ex:
                messagebox.showerror("error",f"Error due to {str(ex)}")




if __name__=="__main__":
    root=Tk() 
    obj=reportclass(root)
    root.mainloop()        