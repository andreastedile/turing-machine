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

    def encode_rule(self, q_i: str, X_j: str, q_k: str, X_l: str, D_m: str) -> str:
        i, j, k, l, m = self.Q.index(q_i) + 1, \
                        self.Γ.index(X_j) + 1, \
                        self.Q.index(q_k) + 1, \
                        self.Γ.index(X_l) + 1, \
                        1 if D_m == 'L' else 2

        return '0' * i + \
               str(10 ** j) + \
               str(10 ** k) + \
               str(10 ** l) + \
               str(10 ** m)

    def encode(self) -> str:
        return '11'.join([self.encode_rule(*k, *v) for k, v in self._δ.items()])
