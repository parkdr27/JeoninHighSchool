import multiprocessing
import time

def sender(pipe):
    for i in range(10):
        msg = f"Message {i}"
        print(f"Sending: {msg}")
        pipe.send(msg)  # 파이프를 통해 메시지를 보냄
        time.sleep(1)  # 1초 대기

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=sender, args=(parent_conn,))
    p.start()

    for _ in range(10):
        received = child_conn.recv()  # 파이프를 통해 메시지를 받음
        print(f"Received in main: {received}")

    p.join()  # sender 프로세스가 종료될 때까지 대기