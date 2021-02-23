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
