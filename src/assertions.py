def type_Q(Q: set):
    assert type(Q) is set, 'Q is not set'
    assert all(type(state) is str for state in Q), 'Some states of Q are not str'


def type_Σ(Σ: set):
    assert type(Σ) is set, 'Σ is not set'
    assert all(type(symbol) is str for symbol in Σ), 'Some input symbols of Σ are not str'


def type_Γ(Γ: set):
    assert type(Γ) is set, 'Γ is not set'
    assert all(type(tape_symbol) is str for tape_symbol in Γ), 'Some tape symbols of Γ are not str'


def type_δ(δ: dict):
    assert type(δ) is dict, 'δ is not dict'
    # Keys
    assert all(type(tup) is tuple for tup in δ.keys()), 'Some keys of δ are not tuples'
    assert all(len(tup) == 2 for tup in δ.keys()), 'Some keys of δ are not 2-tuples'
    assert all(type(tup[0]) is str and type(tup[1]) is str
               for tup in δ.keys()), 'Not all keys of δ are string tuples'
    # Values
    assert all(type(tup) is tuple for tup in δ.values()), 'Some values of δ are not tuples'
    assert all(len(tup) == 3 for tup in δ.values()), 'Some values of δ are not 3-tuples'
    assert all(type(tup[0]) is str and type(tup[1]) is str and type(tup[2]) is str for tup in
               δ.values()), 'Not all values of δ are string tuples'


def type_q_0(q_0: str):
    assert type(q_0) is str, 'q_0 is not str'
    assert q_0 != '', 'q_0 is empty'


def type_B(B: str):
    assert type(B) is str, 'B is not str'


def type_F(F: set):
    assert type(F) is set, 'F is not set'
    assert all(type(state) is str for state in F), 'Some states of F are not str'


def Σ_subset_Γ(Σ: set, Γ: set):
    assert Σ.issubset(Γ), 'Σ is not subset of Γ'


def q_0_member_Q(q_0: str, Q: set):
    assert q_0 in Q, 'q_0 is not in Q'


def B_member_Γ_not_Σ(B: str, Γ: set, Σ: set):
    assert B in Γ, 'B is not in Γ'
    assert B not in Σ.difference(Γ), 'B is in Σ'


def F_subset_Q(F: set, Q: set):
    assert F.issubset(Q), 'F is not subset of Q'


def transitions_δ(δ: dict, Q: set, Γ: set):
    all(q in Q for q, _ in δ.keys())
    all(X in Γ for _, X in δ.keys())

    all(p in Q for p, _, _ in δ.values())
    all(Y in Γ for _, Y, _ in δ.values())
    all(D == 'L' or D == 'R' for _, _, D in δ.values())


def assert_all(Q: set, Σ: set, Γ: set, δ, q_0, B, F: set):
    type_Q(Q)
    type_Σ(Σ)
    type_Γ(Γ)
    type_δ(δ)
    type_q_0(q_0)
    type_B(B)
    type_F(F)

    Σ_subset_Γ(Σ, Γ)
    q_0_member_Q(q_0, Q)
    B_member_Γ_not_Σ(B, Γ, Σ)
    F_subset_Q(F, Q)
    transitions_δ(δ, Q, Γ)
