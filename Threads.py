import threading

counter = 0
iterations = 100000

def increment():
    global counter
    for _ in range(iterations):
        counter += 1

def decrement():
    global counter
    for _ in range(iterations):
        counter -= 1

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=decrement)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(f"Final value of counter: {counter}")
