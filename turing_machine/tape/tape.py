class Tape(list):
    def __init__(self, B: str):
        self.B = B
        super(Tape, self).__init__()

    def __getitem__(self, index: int):
        if index < 0 or index >= len(self):
            return self.B
        return super(Tape, self).__getitem__(index)

    def __setitem__(self, index, value):
        if index == -1:
            self.insert(0, value)
        elif index == len(self):
            self.append(value)
        else:
            super(Tape, self).__setitem__(index, value)
