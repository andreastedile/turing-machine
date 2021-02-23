from src.turing_machine import TuringMachine as TM

Q = {'q_0', 'q_1', 'q_2', 'q_3', 'q_4'}
Σ = {'0', '1'}
Γ = {'0', '1', 'X', 'Y', 'B'}
δ = {
    ('q_0', '0'): ('q_1', 'X', 'R'),
    ('q_0', 'Y'): ('q_3', 'Y', 'R'),

    ('q_1', '0'): ('q_1', '0', 'R'),
    ('q_1', '1'): ('q_2', 'Y', 'L'),
    ('q_1', 'Y'): ('q_1', 'Y', 'R'),

    ('q_2', '0'): ('q_2', '0', 'L'),
    ('q_2', 'X'): ('q_0', 'X', 'R'),
    ('q_2', 'Y'): ('q_2', 'Y', 'L'),

    ('q_3', 'Y'): ('q_3', 'Y', 'R'),
    ('q_3', 'B'): ('q_4', 'B', 'R'),
}

M = TM(Q, Σ, Γ, δ, 'q_0', 'B', {'q_4'})
M.place_input('0011')

print(M.instantaneous_description())
while True:
    try:
        print(next(M))
    except StopIteration as e:
        print(e)
        break
