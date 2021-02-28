from re import compile
from math import log10

from ordered_set import OrderedSet as Set

from turing_machine.utils.assertions import assert_all


class Control:
    regex = compile('^(0+)(10+)(10+)(10+)(10+)$')

    def __init__(self, Q: Set, Σ: Set, Γ: Set, δ: dict, q_0: str, B: str, F: Set):
        assert_all(Q, Σ, Γ, δ, q_0, B, F)

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

    @classmethod
    def dummy(cls):
        return cls(Set('q1'), Set(), Set('B'), dict(), 'q1', 'B', Set())

    @classmethod
    def from_encoding(cls, encoding: str):
        codes = encoding.split('11')

        if any(not bool(Control.regex.match(code)) for code in codes):
            return Control.dummy()

        Q = ['q_1', 'q_2']
        Γ = ['0', '1', 'B']
        δ = dict()

        for code in codes:
            q_i, X_j, q_k, X_l, D_m = Control.regex.match(code).groups()

            i = len(q_i)
            j = int(log10(int(X_j)))
            k = int(log10(int(q_k)))
            l = int(log10(int(X_l)))
            m = int(log10(int(D_m)))

            q_i = f'q_{i}'
            if i - 1 >= len(Q):
                Q.extend([None] * (i - 1 - len(Q)))
                Q.append(q_i)
            elif Q[i - 1] is None:
                Q[i - 1] = q_i

            X_j = f'X_{j}'
            if j - 1 >= len(Γ):
                Γ.extend([None] * (j - 1 - len(Γ)))
                Γ.append(X_j)
            elif Γ[j - 1] is None:
                Γ[j - 1] = X_j

            q_k = f'q_{k}'
            if k - 1 >= len(Q):
                Q.extend([None] * (k - 1 - len(Q)))
                Q.append(q_k)
            elif Q[k - 1] is None:
                Q[k - 1] = q_k

            X_l = f'X_{l}'
            if l - 1 >= len(Γ):
                Γ.extend([None] * (l - 1 - len(Γ)))
                Γ.append(X_l)
            elif Γ[l - 1] is None:
                Γ[l - 1] = X_l

            m = 'L' if m - 1 == 0 else 'R'

            δ[(Q[i - 1], Γ[j - 1])] = (Q[k - 1], Γ[l - 1], m)

        return cls(Set(Q), Set(['0', '1']), Set(Γ), δ, 'q_1', 'B', Set(['q_2']))
