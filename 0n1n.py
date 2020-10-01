from src.turing_machine import TuringMachine as TM

Q = {'q_1', 'q_find1', 'q_goback', 'q_exit', 'q_accept', 'q_reject'}
Σ = {'0', '1'}
Γ = {'0', '1', 'X', 'Y', '⊔'}
δ = {
    'q_1': {
        '0': ('X', 'q_find1', 'R'),
        '1': ('1', 'q_reject', 'S'),
        'X': ('X', 'q_reject', 'S'),
        'Y': ('Y', 'q_exit', 'R'),
        '⊔': ('⊔', 'q_accept', 'S')
    },
    'q_find1': {
        '0': ('0', 'q_find1', 'R'),
        '1': ('Y', 'q_goback', 'L'),
        'X': ('X', 'q_reject', 'S'),
        'Y': ('Y', 'q_find1', 'R'),
        '⊔': ('⊔', 'q_reject', 'S')
    },
    'q_goback': {
        '0': ('0', 'q_goback', 'L'),
        '1': ('1', 'q_reject', 'S'),
        'X': ('X', 'q_1', 'R'),
        'Y': ('Y', 'q_goback', 'L'),
        '⊔': ('⊔', 'q_reject', 'S')
    },
    'q_exit': {
        '0': ('0', 'q_reject', 'S'),
        '1': ('1', 'q_reject', 'S'),
        'X': ('X', 'q_reject', 'S'),
        'Y': ('Y', 'q_exit', 'R'),
        '⊔': ('⊔', 'q_accept', 'S')
    }
}

M = TM(Q, Σ, Γ, δ, 'q_1', 'q_accept', 'q_reject')
M.write_string('0011')

M = iter(M)
while True:
    print(M)
    try:
        next(M)
    except StopIteration as e:
        print(e)
        break
