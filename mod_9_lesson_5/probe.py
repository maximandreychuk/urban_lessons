import time


def stutter_faactory(func):
    def wrapper(line):
        start = time.time()
        res = func(line)
        end = time.time()
        dif = end - start
        return f"line: {(res+' ')*234}, time {dif}"
    return wrapper


@stutter_faactory
def stutter(line):
    return line[:2] + '-' + line


st = stutter("mvideo")
print(st)
