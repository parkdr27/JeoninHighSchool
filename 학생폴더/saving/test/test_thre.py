import threading
import tkinter as tk
import time

class TestApp:
    
    @staticmethod
    def test(a, b): 
        for i in range(a):
            print("통과")
            print(b)
            time.sleep(1)  # 조금 지연을 줘서 출력이 확인되도록 함

    @staticmethod
    def wep():
        window = tk.Tk()
        window.title("Tkinter Window")
        window.geometry("300x200")
        
        # 버튼 추가 예시
        label = tk.Label(window, text="This is a tkinter window.")
        label.pack(pady=20)
        
        window.mainloop()

# 스레드를 사용하여 `test` 메서드 실행
a = threading.Thread(target=TestApp.test, args=(5, 10))
a.start()

# GUI는 메인 스레드에서 실행
TestApp.wep()

