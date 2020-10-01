from itertools import product


def domain(Q: set, Γ: set, q_accept: str, q_reject: str):
    dom = Q.copy()
    dom.remove(q_accept)
    dom.remove(q_reject)
    dom = set(product(dom, Γ))
    return dom


def codomain(Γ: set, Q: set):
    cod = set(product(Γ, Q, {'L', 'R', 'S'}))
    return cod
