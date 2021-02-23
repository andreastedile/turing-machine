from turingmachine.assertions import assert_all


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


class Control:
    def __init__(self, Q: set, Σ: set, Γ: set, δ: dict, q_0: str, B: str, F: set):
        self.Q = Q
        self.Σ = Σ
        self.Γ = Γ
        self._δ = δ
        self.q_0 = q_0
        self.B = B
        self.F = F

        self.q = self.q_0  # current state

    def δ(self, q, X) -> tuple:
        return self._δ[(q, X)]


class TuringMachine:
    def __init__(self, Q: set, Σ: set, Γ: set, δ: dict, q_0: str, B: str, F: set):
        assert_all(Q, Σ, Γ, δ, q_0, B, F)

        self.control = Control(Q, Σ, Γ, δ, q_0, B, F)
        self.tape = Tape(B)
        self.tape_head = 0

    def place_input(self, string: str):
        assert type(string) is str, 'input is not str'
        for symbol in string:
            self.tape.append(symbol)

    def instantaneous_description(self) -> str:
        tape_symbols = self.tape.copy()
        tape_symbols.insert(self.tape_head, self.control.q)
        return ' '.join(tape_symbols)

    def __next__(self):
        q = self.control.q  # current state
        X = self.tape[self.tape_head]  # current symbol

        if q in self.control.F:
            raise StopIteration('Accept')

        try:
            # p is the next state, in Q
            # Y is the symbol, in Γ, written in the cell being scanned, replacing whatever symbol was there
            # D is a direction, either L or R, standing for "left" or "right," respectively,
            # and telling us the direction in which the head moves.
            p, Y, D = self.control.δ(q, X)
        except KeyError:
            raise StopIteration('Reject')

        self.control.q = p

        self.tape[self.tape_head] = Y
        if D == 'L':
            self.tape_head -= 1
        elif D == 'R':
            self.tape_head += 1
        # S means "Stay"

        return self.instantaneous_description()

    def __iter__(self):
        return self
