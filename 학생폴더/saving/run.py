import subprocess

def run_script(script_name):
    subprocess.run(["python", script_name])

if __name__ == "__main__":
    from multiprocessing import Process

    scripts = ["main1.py", "main2.py"]
    processes = []

    for script in scripts:
        p = Process(target=run_script, args=(script,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()