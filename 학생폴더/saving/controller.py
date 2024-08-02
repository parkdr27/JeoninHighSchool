import multiprocessing
import time

def sender(pipe):
    for i in range(10):
        msg = f"Message {i}"
        print(f"Sending: {msg}")
        pipe.send(msg)
        time.sleep(1)
    pipe.send("STOP")

def receiver(pipe):
    while True:
        msg = pipe.recv()
        if msg == "STOP":
            break
        print(f"Received: {msg}")

if __name__ == "__main__":
    parent_conn, child_conn = multiprocessing.Pipe()

    sender_process = multiprocessing.Process(target=sender, args=(parent_conn,))
    receiver_process = multiprocessing.Process(target=receiver, args=(child_conn,))

    sender_process.start()
    receiver_process.start()

    sender_process.join()
    receiver_process.join()
