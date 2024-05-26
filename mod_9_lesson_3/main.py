class EvenNumbers():
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def __iter__(self):
        self.cnt = self.start-1
        return self

    def __next__(self):
        if self.cnt >= self.end:
            raise StopIteration
        self.cnt += 1
        if self.cnt % 2 == 0:
            return self.cnt


ev = EvenNumbers(10, 25)
for i in ev:
    if i is not None:
        print(i)
