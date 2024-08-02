import multiprocessing

def receiver(pipe):
    while True:
        msg = pipe.recv()  # 파이프를 통해 메시지를 받음
        if msg == "STOP":
            break  # "STOP" 메시지를 받으면 루프를 종료
        print(f"Received: {msg}")

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()
    p = multiprocessing.Process(target=receiver, args=(child_conn,))
    p.start()

    for i in range(10):
        msg = f"Message {i}"
        print(f"Sending in main: {msg}")
        parent_conn.send(msg)  # 파이프를 통해 메시지를 보냄

    parent_conn.send("STOP")  # "STOP" 메시지를 보냄으로써 수신 측 프로세스를 종료시킴
    p.join()  # receiver 프로세스가 종료될 때까지 대기