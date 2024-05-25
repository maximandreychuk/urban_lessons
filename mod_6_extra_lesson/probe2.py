class Mode():

    def __init__(self, title, ismajor):
        self.title = title
        self.ismajor = True

    def get_title(self):
        return self.title

    def __str__(self):
        return "Title: {}, Major: {}".format(self.title, self.ismajor)


class Mode2(Mode):

    pass


mode1 = Mode("Ionian", "Major")
print(mode1)

mode2 = Mode2("Dorian", "Minor")
print(mode2.get_title())
