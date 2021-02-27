from ordered_set import OrderedSet as Set

from turing_machine.utils.assertions import assert_all
from turing_machine.control.control import Control
from turing_machine.tape.tape import Tape


class TuringMachine:
    def __init__(self, Q: Set, Σ: Set, Γ: Set, δ: dict, q_0: str, B: str, F: Set):
        assert_all(Q, Σ, Γ, δ, q_0, B, F)

        self.control = Control(Q, Σ, Γ, δ, q_0, B, F)
        self.tape = Tape(B)
        self.tape_head = 0

    def place_input(self, string: str):
        assert type(string) is str, 'input is not str'
        for symbol in string:
            self.tape.append(symbol)

    def resume(self, instantaneous_description: list):
        assert len(self.tape) == 0, 'tape is not empty'
        assert type(instantaneous_description) is list, 'instantaneous description is not list'

        tape_symbols = [tape_symbol for tape_symbol in instantaneous_description if tape_symbol in self.control.Γ]
        assert len(tape_symbols) == len(instantaneous_description) - 1, \
            'length of tape symbols is not length of instantaneous description - 1'
        assert all(tape_symbol in self.control.Γ for tape_symbol in tape_symbols), \
            'not all tape symbols are in Γ'

        q = (Set(instantaneous_description) - Set(tape_symbols)).pop()  # current state
        assert q in self.control.Q, 'q is not in Q'

        for tape_symbol in tape_symbols:
            self.tape.append(tape_symbol)
        self.control.q = q
        self.tape_head = instantaneous_description.index(q)

    def instantaneous_description(self) -> list:
        tape_symbols = self.tape.copy()
        tape_symbols.insert(self.tape_head, self.control.q)
        return tape_symbols

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
