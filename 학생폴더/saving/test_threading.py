import tkinter as tk
import threading
import time

def long_task():
    label.config(text="작업 중...")
    
    # 긴 작업 수행 (5초 동안 카운트)
    for i in range(5):
        time.sleep(1)
        print(f"{i+1}초 경과")

    label.config(text="작업 완료!")

def on_button_click():
    # 긴 작업을 스레드로 실행하여 UI 멈춤 방지
    threading.Thread(target=long_task).start()

# Tkinter 윈도우 설정
root = tk.Tk()
root.title("Tkinter 스레드 예시")

# 레이블과 버튼 설정
label = tk.Label(root, text="버튼을 클릭하세요.")
label.pack(pady=10)

button = tk.Button(root, text="작업 시작", command=on_button_click)
button.pack(pady=10)

# Tkinter 메인 루프
root.mainloop()
