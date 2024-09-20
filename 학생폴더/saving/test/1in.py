import tkinter

class hatchocko:
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("창 변경 예제")
        self.geometry("800x420")
        self.tn = 0
        self.count = 0
        self.total = 0
        self.frame1 = tkinter.Frame(self)
        self.frame2 = tkinter.Frame(self)
        self.create_frame1()
        self.create_frame2()
    
    def create_frame1(self):
        button = tkinter.Button(self.frame1, text="123456789",width=3, height= 4, command=self.sinw1)
        button.pack()


    def create_frame2(self):
        label=tkinter.Label(self.frame2,text="987654321",width=3, height= 4 )
    def sinw1(self):
        x=input("test test test")
        self.create_frame2
        
    def sow_faem(self):
        self.fraem1.pack
        self.fraem2.pack_forget

if __name__ == "__main__":
    d4c = hatchocko()
    d4c.mainloop()