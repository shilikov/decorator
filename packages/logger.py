from datetime import datetime
from time import time
from pprint import pprint

def log_to_console(func):
    def loger(*args, **kwargs):
        date = datetime.date(datetime.now())
        times = datetime.time(datetime.now())
        func_name = func.__name__
        started_at = time()
        result = func(*args, **kwargs)
        ended_at = time()
        elapsed = round(ended_at - started_at, 4)
        print()

        pprint(
            f"date: {date}\n"
              f"time: {times}\n"
              f"name: {func_name}\n"
              f"args: {args, kwargs}\n"
              f"result: {result}\n"
              f'функция работала {elapsed} секунд(ы)'
              )


        return result
    return loger

def log_to_file(log_file):
    def decor(func):
        def loger(*args, **kwargs):
            date = datetime.date(datetime.now())
            times = datetime.time(datetime.now())
            func_name = func.__name__
            started_at = time()
            result = func(*args, **kwargs)
            ended_at = time()
            elapsed = round(ended_at - started_at, 4)
            

            with open(log_file, 'a', encoding='utf-8') as file:
                file.write(
                        f"date: {date}\n"
                           f"time: {times}\n"
                           f"name: {func_name}\n"
                           f"args: {args, kwargs}\n"
                           f"result: {result}\n"
                           f'функция работала {elapsed} секунд(ы)\n\n'
                           )

            return result
        return loger
    return decor
