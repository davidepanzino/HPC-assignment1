import threading
import subprocess
import time

def script1(start_time):
    print(f"Thread 1 started at: {time.time() - start_time:.2f} seconds")
    subprocess.call(['python3', 'JuliaSet.py'])
    print(f"Thread 1 finished at: {time.time() - start_time:.2f} seconds")

def script2(start_time):
    print(f"Thread 2 started at: {time.time() - start_time:.2f} seconds")
    subprocess.call(['python3', 'percentages.py'])
    print(f"Thread 2 finished at: {time.time() - start_time:.2f} seconds")

if __name__ == '__main__':
    # Record the start time of the program
    start_time = time.time()

    # Launch thread2
    thread2 = threading.Thread(target=script2, args=(start_time,))
    thread2.start()

    # Wait for 1 seconds
    print("Waiting for 1 seconds before launching thread1...")
    time.sleep(1)

    # Launch thread1
    thread1 = threading.Thread(target=script1, args=(start_time,))
    thread1.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

