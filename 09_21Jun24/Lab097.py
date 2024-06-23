import time


def note_time_Decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        #log_function()
        func()
        end_time = time.time()
        print("time taken "+str(end_time-start_time))
    return wrapper()


@note_time_Decorator
def log_function():
    time.sleep(5)
    print("Print the logs of time taken")

@note_time_Decorator
def reporting_function():
    time.sleep(2)
    print("Print the logs of time taken")