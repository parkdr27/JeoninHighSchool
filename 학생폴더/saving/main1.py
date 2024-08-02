import tkinter


lidar_data = ((0,), (0,))
sensor_data = (0, 0, 0, 0, 0)
rplidar = None
ser = None
state = "ready"

sensor_stop = True
is_print = True


class test(tkinter.Tk):
    global tomsky

    def __init__(self):
        tkinter.Tk.__init__(self)

        self.title("창 변경 예제")
        self.geometry("800x420")
        self.tn = 0
        self.count = 0
        self.total = 0
        self.li = [0, 0, 0, 0, self.count]
        self.li1 = self.li
        self.li2 = self.li
        self.li3 = self.li
        self.li4 = self.li
        self.total1 = 0
        self.total2 = 0
        self.total3 = 0
        self.total4 = 0

        self.frame1 = tkinter.Frame(self)
        self.frame2 = tkinter.Frame(self)
        self.frame3 = tkinter.Frame(self)
        self.frame4 = tkinter.Frame(self)
        self.frame5 = tkinter.Frame(self)
        self.frame6 = tkinter.Frame(self)
        self.frame7 = tkinter.Frame(self)
        self.frame8 = tkinter.Frame(self)
        self.frame9 = tkinter.Frame(self)
        self.frame10 = tkinter.Frame(self)
        self.frame11 = tkinter.Frame(self)
        self.frame12 = tkinter.Frame(self)

        self.create_frame1()
        self.create_frame2()
        self.create_frame3()
        self.create_frame4()
        self.create_frame5()
        self.create_frame6()
        self.create_frame7()
        self.create_frame8()
        self.create_frame9()
        self.create_frame10()
        self.create_frame11()
        self.create_frame12()

        self.show_frame1()
        for self.tn in range(1,4):
            self.reset()
    # create frame뒤 에 숫자당 해당 프레임 생성 코드

    def create_frame1(self):  # 서비스 선택1
        label = tkinter.Label(self.frame1, text="명령할 서비스", width=33,
                              height=2, fg="red", relief="solid", font=("Helvetica", 25))
        button = tkinter.Button(self.frame1, overrelief="solid", background="red", foreground="white",
                                text="서빙", width=8, height=5, command=self.show_frame5, repeatdelay=1000, repeatinterval=100, font=("Helvetica", 25))
        button1 = tkinter.Button(self.frame1, overrelief="solid", background="blue", foreground="white",
                                 text="주문 및\n계산", width=8, height=5, command=self.show_frame4, repeatdelay=1000, repeatinterval=100, font=("Helvetica", 25))
        button2 = tkinter.Button(self.frame1, overrelief="solid",
                                 text="전원", width=3, height=1, command=self.out, foreground="red", repeatdelay=1000, repeatinterval=100, font=("Helvetica", 25))
        label.place(x=85, y=0)
        button.place(x=110, y=100)
        button1.place(x=530, y=100)
        button2.place(x=370, y=350)

        self.frame1.pack(fill=tkinter.BOTH, expand=True)

    def create_frame2(self):  # 서비스 선택 2
        label = tkinter.Label(self.frame2, text="원하시는 서비스를 선택해주세요", width=30,
                              height=2, fg="red", relief="solid", font=("Helvetica", 25))
        button = tkinter.Button(self.frame2, overrelief="solid", background="red", foreground="white", command=self.show_frame6,
                                text="주문", width=8, height=4, repeatdelay=1000, repeatinterval=100, font=("Helvetica", 25))
        button1 = tkinter.Button(self.frame2, overrelief="solid", background="blue", foreground="white", command=self.show_frame3,
                                 text="계산", width=8, height=4, repeatdelay=1000, repeatinterval=100, font=("Helvetica", 25))
        button2 = tkinter.Button(self.frame2, overrelief="solid", background="black", foreground="white", command=lambda: (self.show_frame11(), self.save()),
                                 text="돌려보내기", width=8, height=2, repeatdelay=1000, repeatinterval=100, font=("Helvetica", 25))

        label.pack()
        label.place(x=85, y=0)
        button.place(x=110, y=100)
        button1.place(x=470, y=100)
        button2.place(x=290, y=280)

    def create_frame3(self):  # 결제
        kth = tkinter.Label(self.frame3, width=60, height=25, relief="solid")
        total = tkinter.Label(self.frame3, width=15, height=3, background="red",
                              text="총액:", fg="white", relief="solid", font=("Helvetica", 20))
        self.sow = tkinter.Label(self.frame3, width=15, height=3, text=(
            str(self.li[4])+"원"), fg="black", relief="solid", font=("Helvetica", 20))
        buybutton = tkinter.Button(self.frame3, fg="white", overrelief="solid", width=15, height=3,
                                   text="결제", borderwidth=4, repeatdelay=1000, repeatinterval=100, command=lambda: (self.show_frame12()), background="red", font=("Helvetica", 20))
        self.GER = tkinter.Label(
            self.frame3, text="라면                             0개 총 0원", font=("Helvetica", 12))
        self.SOV = tkinter.Label(
            self.frame3, text="떡볶이                           0개 총 0원", font=("Helvetica", 12))
        self.ENG = tkinter.Label(
            self.frame3, text="콜라                             0개 총 0원", font=("Helvetica", 12))
        self.JAP = tkinter.Label(
            self.frame3, text="아이스 아메리카노 0개 총 0원", font=("Helvetica", 12))

        back = tkinter.Button(self.frame3, overrelief="solid",
                              text="돌아가기", command=self.show_frame2)
        self.GER.place(x=40, y=30)
        self.SOV.place(x=40, y=70)
        self.ENG.place(x=40, y=110)
        self.JAP.place(x=40, y=150)
        back.place(x=5, y=5)
        buybutton.place(x=512, y=270)
        total.place(x=512, y=20)
        kth.place(x=20, y=20)
        self.sow.place(x=512, y=150)

    def create_frame4(self):  # 테이블 보내는 용
        label = tkinter.Label(self.frame4,  text="서빙 로봇을 보낼 테이블을 고르세요", width=30,
                              height=2, fg="red", relief="solid", font=("Helvetica", 25))
        button1 = tkinter.Button(self.frame4, overrelief="solid", background="blue", foreground="white", command=lambda: (self.chomun(1), self.show_frame10()),
                                 text="1번 테이블", width=8, height=2, repeatdelay=1000, repeatinterval=100, font=("Helvetica", 23))
        button2 = tkinter.Button(self.frame4, overrelief="solid", background="blue", foreground="white", command=lambda: (self.chomun(2), self.show_frame10()),
                                 text="2번 테이블", width=8, height=2, repeatdelay=1000, repeatinterval=100, font=("Helvetica", 23))
        button3 = tkinter.Button(self.frame4, overrelief="solid", background="blue", foreground="white", command=lambda: (self.chomun(3), self.show_frame10()),
                                 text="3번 테이블", width=8, height=2, repeatdelay=1000, repeatinterval=100, font=("Helvetica", 23))
        button4 = tkinter.Button(self.frame4, overrelief="solid", background="blue", foreground="white", command=lambda: (self.chomun(4), self.show_frame10()),
                                 text="4번 테이블", width=8, height=2, repeatdelay=1000, repeatinterval=100, font=("Helvetica", 23))
        back = tkinter.Button(self.frame4, overrelief="solid",
                              text="돌아가기", command=self.show_frame1)

        label.pack()
        button1.place(x=120, y=100)
        button2.place(x=515, y=100)
        button3.place(x=120, y=300)
        button4.place(x=515, y=300)
        back.place(x=10, y=10)

    def create_frame5(self):  # 서빙
        label = tkinter.Label(self.frame5, text="서빙 로봇을 보낼 테이블을 고르세요", width=30,
                              height=2, fg="red", relief="solid", font=("Helvetica", 25))
        button1 = tkinter.Button(self.frame5, overrelief="solid", background="blue", foreground="white", command=lambda: (self.chomun(1), self.show_frame7()),
                                 text="1번 테이블", width=8, height=2, repeatdelay=1000, repeatinterval=100, font=("Helvetica", 25))
        button2 = tkinter.Button(self.frame5, overrelief="solid", background="blue", foreground="white", command=lambda: (self.chomun(2), self.show_frame7()),
                                 text="2번 테이블", width=8, height=2, repeatdelay=1000, repeatinterval=100, font=("Helvetica", 25))
        button3 = tkinter.Button(self.frame5, overrelief="solid", background="blue", foreground="white", command=lambda: (self.chomun(3), self.show_frame7()),
                                 text="3번 테이블", width=8, height=2, repeatdelay=1000, repeatinterval=100, font=("Helvetica", 25))
        button4 = tkinter.Button(self.frame5, overrelief="solid", background="blue", foreground="white", command=lambda: (self.chomun(4), self.show_frame7()),
                                 text="4번 테이블", width=8, height=2, repeatdelay=1000, repeatinterval=100, font=("Helvetica", 25))
        back = tkinter.Button(self.frame5, overrelief="solid",
                              text="돌아가기", command=self.show_frame1)
        label.pack()
        button1.place(x=120, y=100)
        button2.place(x=515, y=100)
        button3.place(x=120, y=300)
        button4.place(x=515, y=300)
        back.place(x=10, y=10)

    def create_frame6(self):  # 주문
        global tomsky
        Yezhov = tkinter.Label(
            self.frame6, text="주문하실 음식을 선택해주세요", font=("Helvetica", 20))
        Trotsky = tkinter.Button(self.frame6, text="라면 2000원", width=30, height=2, fg="red", relief="solid", font=("Helvetica", 20),
                                 command=lambda: self.countUP("la"))
        Bukharin = tkinter.Button(self.frame6, text="콜라 1000원", width=30, height=2, fg="red", relief="solid", font=("Helvetica", 20),
                                  command=lambda: self.countUP("co"))
        Tukhachevsky = tkinter.Button(self.frame6, text="떡볶이 3500원", width=30, height=2, fg="red", relief="solid", font=("Helvetica", 20),
                                      command=lambda: self.countUP("duc"))
        Zinoviev = tkinter.Button(self.frame6, text="아이스 아메리카노 4000원", width=30, height=2, fg="red", relief="solid", font=("Helvetica", 20),
                                  command=lambda: self.countUP("t34"))
        tomsky = tkinter.Label(
            self.frame6, text="총액 0 원", font=("Helvetica", 20))
        back = tkinter.Button(self.frame6, overrelief="solid",
                              text="돌아가기", command=self.show_frame2)

        Yezhov.pack()
        Trotsky.pack()
        Bukharin.pack()
        Tukhachevsky.pack()
        Zinoviev.pack()
        tomsky.pack()
        back.place(x=5, y=5)

    def create_frame7(self):  # 음식가는거 도착

        Ideal = tkinter.Label(self.frame7, text="서빙로봇이 음식을 운반 중입니다.", width=30,
                              height=2, fg="red", relief="solid", font=("Helvetica", 25))
        Ideal.pack()
        loding = tkinter.Button(self.frame7,  overrelief="solid", background="blue", width=30,
                                height=2, text="도착", foreground="white",  command=self.show_frame9)

        loding.pack()

        loding.pack()

    def create_frame8(self):
        label = tkinter.Label(self.frame8, text="서빙로봇이 돌아가는 중입니다.", width=30,
                              height=2, fg="red", relief="solid", font=("Helvetica", 25))
        but = tkinter.Button(self.frame8, overrelief="solid", background="blue", width=30,
                             height=2, text="도착", foreground="white", command=self.show_frame1)

        label.pack()
        but.pack()

    def create_frame9(self):  # 음식 받고 돌려보네는 창
        label = tkinter.Label(self.frame9,   text="음식 배송이 완료되었습니다. \n음식을 가져가 주세요.", width=34,
                              height=3, fg="red", relief="solid", font=("Helvetica", 20))
        but = tkinter.Button(self.frame9,  overrelief="solid", background="blue", width=30,
                             height=2, text="돌려보내기", foreground="white", command=self.show_frame8)

        label.pack()
        but.pack()

    def create_frame10(self):
        label = tkinter.Label(self.frame10, text="서빙로봇이 이동 중입니다.", width=30,
                              height=2, fg="red", relief="solid", font=("Helvetica", 25))
        but = tkinter.Button(self.frame10, overrelief="solid", background="blue", width=30,
                             height=2, text="도착", foreground="white", command=self.show_frame2)

        label.pack()
        but.pack()

    def create_frame11(self):  # 돌아올때 도착 뜨는창
        labal = tkinter.Label(self.frame11,  text="서빙로봇이 돌아가는 중입니다.", width=30,
                              height=2, fg="red", relief="solid", font=("Helvetica", 25))
        but = tkinter.Button(self.frame11,  overrelief="solid", background="blue", width=30,
                             height=2, text="도착", foreground="white", command=self.show_frame1)

        labal.pack()
        but.pack()

    def create_frame12(self):
        label = tkinter.Label(self.frame12, text="결제가 완료 되었습니다.",
                              width=30, height=2, relief="solid")
        but = tkinter.Button(self.frame12, overrelief="solid", background="blue", width=30,
                             height=2, text="돌아오기", foreground="white", command=lambda: (self.reset(), self.show_frame8()))
        label.pack()
        but.pack()

    # 해당 showframe 뒤에 숫자 당 보여주는 것을 의미

    def show_frame1(self):

        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame7.pack_forget()
        self.frame8.pack_forget()
        self.frame9.pack_forget()
        self.frame10.pack_forget()
        self.frame11.pack_forget()
        self.frame1.pack(fill=tkinter.BOTH, expand=True)  # 첫 번째 창 표시
        self.frame12.pack_forget()

    def show_frame2(self):
        self.frame1.pack_forget()
        self.frame10.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame7.pack_forget()
        self.frame8.pack_forget()
        self.frame9.pack_forget()
        self.frame2.pack(fill=tkinter.BOTH, expand=True)  # 두 번째 창 표시
        print(self.tn)
        self.frame11.pack_forget()
        self.frame12.pack_forget()

    def show_frame3(self):

        print(self.li)
        self.sow.config(text="전체 총합: " + str(self.count) + "원")
        self.GER.config(text="라면                           " +
                        str(int(self.li[0]/2000))+"개 총 " + str(self.li[0]) + "원")
        self.SOV.config(text="떡볶이                         " +
                        str(int(self.li[2]/3500))+"개 총 " + str(self.li[2]) + "원")
        self.ENG.config(text="콜라                           " +
                        str(int(self.li[1]/1000))+"개 총 " + str(self.li[1]) + "원")
        self.JAP.config(text="아이스 아메리카노               " +
                        str(int(self.li[3]/4000)) + "개 총 " + str(self.li[3]) + "원")

        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame11.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame7.pack_forget()
        self.frame8.pack_forget()
        self.frame9.pack_forget()
        self.frame3.pack(fill=tkinter.BOTH, expand=True)
        self.frame10.pack_forget()
        self.frame12.pack_forget()

    def show_frame4(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame11.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame7.pack_forget()
        self.frame8.pack_forget()
        self.frame9.pack_forget()
        self.frame4.pack(fill=tkinter.BOTH, expand=True)
        self.frame10.pack_forget()
        self.frame12.pack_forget()

    def show_frame5(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame11.pack_forget()
        self.frame6.pack_forget()
        self.frame7.pack_forget()
        self.frame8.pack_forget()
        self.frame9.pack_forget()
        self.frame5.pack(fill=tkinter.BOTH, expand=True)  # 다섯 번째 창 표시
        self.frame10.pack_forget()
        self.frame12.pack_forget()

    def show_frame6(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame11.pack_forget()
        self.frame7.pack_forget()
        self.frame8.pack_forget()
        self.frame9.pack_forget()
        self.frame2.pack_forget()  # 두 번째 창 숨기기
        self.frame6.pack(fill=tkinter.BOTH, expand=True)  # 여섯 번째 창 표시
        self.frame10.pack_forget()
        self.frame12.pack_forget()

    def show_frame7(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame11.pack_forget()
        self.frame6.pack_forget()
        self.frame8.pack_forget()
        self.frame9.pack_forget()

        self.frame7.pack(fill=tkinter.BOTH, expand=True)  # 여섯 번째 창 표시\
        self.frame10.pack_forget()
        self.frame12.pack_forget()

    def show_frame8(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame11.pack_forget()
        self.frame6.pack_forget()
        self.frame9.pack_forget()
        self.frame7.pack_forget()
        self.frame9.pack_forget()
        self.frame8.pack(fill=tkinter.BOTH, expand=True)  # 여섯 번째 창 표시\
        self.frame10.pack_forget()
        self.frame12.pack_forget()

    def show_frame9(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame10.pack_forget()
        self.frame6.pack_forget()
        self.frame8.pack_forget()
        self.frame7.pack_forget()
        self.frame11.pack_forget()
        self.frame9.pack(fill=tkinter.BOTH, expand=True)  # 여섯 번째 창 표시\
        self.frame12.pack_forget()

    def show_frame10(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame8.pack_forget()
        self.frame7.pack_forget()
        self.frame9.pack_forget()
        self.frame10.pack(fill=tkinter.BOTH, expand=True)  # 여섯 번째 창 표시\
        self.frame11.pack_forget()
        self.frame12.pack_forget()
        

    def show_frame11(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame8.pack_forget()
        self.frame7.pack_forget()
        self.frame9.pack_forget()
        self.frame11.pack(fill=tkinter.BOTH, expand=True)  # 여섯 번째 창 표시\
        self.frame10.pack_forget()
        self.frame12.pack_forget()

    def show_frame12(self):
        self.frame1.pack_forget()
        self.frame2.pack_forget()
        self.frame3.pack_forget()
        self.frame4.pack_forget()
        self.frame5.pack_forget()
        self.frame6.pack_forget()
        self.frame8.pack_forget()
        self.frame7.pack_forget()
        self.frame9.pack_forget()
        self.frame12.pack(fill=tkinter.BOTH, expand=True)  # 여섯 번째 창 표시\
        self.frame10.pack_forget()
        self.frame11.pack_forget()

    def chomun(self, tbnum):
        q = tbnum
        if q == 1:
            self.tn = 1
            self.load()
        elif q == 2:
            self.tn = 2
            self.load()
        elif q == 3:
            self.tn = 3
            self.load()
        else:
            self.tn = 4
            self.load()

    def load(self):
        if self.tn == 1:

            self.count = self.total1
            self.li = self.li1
            print(self.li)

        elif self.tn == 2:
            self.count = self.total2
            self.li = self.li2
        elif self.tn == 3:
            self.count = self.total3
            self.li = self.li3
        else:
            self.count = self.total4
            self.li = self.li4
        self.sow.config(text="전체 총합: " + str(self.count) + "원")
        tomsky.config(text="전체 총합: " + str(self.count) + "원")

    def save(self):  # 저장용
        if self.tn == 1:
            self.li1 = self.li
            self.total1 = self.li[4]
            print(self.li1)
            print("총액")
            print(self.total1)

            self.count = 0
            self.li = [0, 0, 0, 0, self.count]
            print(self.li)
        elif self.tn == 2:
            self.li2 = self.li
            self.total2 = self.li[4]
            self.count = 0
            self.li = [0, 0, 0, 0, self.count]
            print(self.li)
            print(self.li2)
        elif self.tn == 3:
            self.li3 = self.li
            self.total3 = self.li[4]
            self.count = 0
            self.li = [0, 0, 0, 0, self.count]
            print(self.li)

            print(self.li3)
        else:
            self.li4 = self.li
            self.total4 = self.li[4]
            self.count = 0
            self.li = [0, 0, 0, 0, self.count]
            print(self.li)
            print(self.li4)

    def countUP(self, a):  # 계산처리

        if a == "la":
            self.count += 2000
            self.li[0] += 2000
        elif a == "co":
            self.count += 1000
            self.li[1] += 1000
        elif a == "duc":
            self.count += 3500
            self.li[2] += 3500
        else:
            self.count += 4000
            self.li[3] += 4000
        self.li[4] = self.count
        print(self.li)
        tomsky.config(text="전체 총합: " + str(self.count) + "원")

    def out(self):
        app.destroy()

    def reset(self):
        self.count = 0
        self.li = [0, 0, 0, 0, self.count]
        if self.tn == 1:
            self.li1 = self.li
        elif self.tn == 2:
            self.li2 = self.li
        elif self.tn == 3:
            self.li3 = self.li
        else:
            self.li4 = self.li
        self.save()



if __name__ == "__main__":
    app = test()
    app.mainloop()

    