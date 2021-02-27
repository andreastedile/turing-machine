from ordered_set import OrderedSet as Set


class Control:
    def __init__(self, Q: Set, Σ: Set, Γ: Set, δ: dict, q_0: str, B: str, F: Set):
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
