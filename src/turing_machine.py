from src.checks import check_Q, check_Σ, check_Γ, check_δ, check_w


class Tape(list):
    def __getitem__(self, index: int):
        if index < 0 or index >= len(self):
            return '⊔'
        return super(Tape, self).__getitem__(index)


class TuringMachine:
    def __init__(self, Q: set, Σ: set, Γ: set, δ, q_1, q_accept, q_reject):
        check_Q(Q, q_1, q_accept, q_reject)
        check_Σ(Σ)
        check_Γ(Γ, Σ)
        check_δ(δ, Q, Γ, q_accept, q_reject)

        self.Q = Q
        self.Σ = Σ
        self.Γ = Γ
        self.δ = δ
        self.q_1 = q_1
        self.q_accept = q_accept
        self.q_reject = q_reject

        self.current_state = self.q_1
        self.tape = Tape()
        self.head = 0

    def __str__(self):
        """Returns an Instantaneous Description"""
        tape = self.tape.copy()
        tape.insert(self.head, self.current_state)
        return ' '.join(tape)

    def move_head_left(self):
        """Moves the head to the left"""
        if self.head == 0:
            self.tape.insert(0, '⊔')
        else:
            self.head -= 1

    def move_head_right(self):
        """Moves the head to the right"""
        if self.head == len(self.tape) - 1:
            self.tape.append('⊔')
        self.head += 1

    @property
    def symbol(self):
        return self.tape[self.head]

    @symbol.setter
    def symbol(self, new_symbol):
        self.tape[self.head] = new_symbol

    def write_string(self, w: str):
        check_w(w)
        for symbol in w:
            self.tape.append(symbol)

    def __next__(self):
        if self.current_state == self.q_reject:
            raise StopIteration(f'-> {self.q_reject}: {self}')
        if self.current_state == self.q_accept:
            raise StopIteration(f'-> {self.q_accept}: {self}')

        # The machine does not have a transition for the read symbol
        if self.symbol not in self.δ[self.current_state]:
            raise StopIteration(f'-> {self.q_reject}: δ has no transition for state {self}')

        new_symbol, next_state, direction = self.δ[self.current_state][self.symbol]
        self.symbol = new_symbol
        self.current_state = next_state
        if direction == 'L':
            self.move_head_left()
        elif direction == 'R':
            self.move_head_right()
        # S means "Stay"

    def __iter__(self):
        return self
