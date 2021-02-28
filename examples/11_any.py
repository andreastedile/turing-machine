from turing_machine.turing_machine.turing_machine import TuringMachine as TM

# Hopcroft, p. 380

M = TM.from_encoding('01001000101001100010101001001100010010010100110001000100010010')

M.place_input('110')

print(M.instantaneous_description())
while True:
    try:
        print(next(M))
    except StopIteration as e:
        print(e)
        break
