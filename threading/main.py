import threading
from concurrent.futures import ThreadPoolExecutor


def threaded_function():
    for number in range(3):
        print(f"Printing from {threading.current_thread().name}. {number=}")


with ThreadPoolExecutor(max_workers=10, thread_name_prefix="Worker") as executor:
    for _ in range(10):
        executor.submit(threaded_function)
