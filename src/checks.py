from src.utils import domain, codomain


def check_Q(Q: set, q_1: str, q_accept: str, q_reject: str):
    """
    Exits the program if Q, q_1, q_accept and q_reject are not valid
    :param Q: States
    :param q_1: Starting state
    :param q_accept: Accepting state
    :param q_reject: Rejecting state
    """
    if type(Q) is not set:
        exit('Q is not set')

    if type(q_1) is not str:
        exit(f'q_1 is not str (found: {type(q_1)})')
    if q_1 == '':
        exit('q_1 is empty')
    if q_1 not in Q:
        exit('Q does not contain q_1')

    if type(q_accept) is not str:
        exit('q_accept is not str')
    if q_accept == '':
        exit('q_accept is empty')
    if q_accept not in Q:
        exit('Q does not contain q_accept')

    if type(q_reject) is not str:
        exit('q_reject is not str')
    if q_reject == '':
        exit('q_reject is empty')
    if q_reject not in Q:
        exit('Q does not contain q_reject')

    if q_accept not in Q:
        exit(f'{q_accept} is not in Q')
    if q_reject not in Q:
        exit(f'{q_reject} is not in Q')
    for state in Q:
        if type(state) is not str:
            exit(f'State is not str (found: {type(state)})')
        if state == '':
            exit('State is empty')


def check_Σ(Σ: set):
    """
    Exits the program if Σ is not valid
    :param Σ: Input alphabet
    """
    if type(Σ) is not set:
        exit('Σ is not a set')
    for symbol in Σ:
        if type(symbol) is not str:
            exit(f'Symbol is not str (found: {type(symbol)})')
        if symbol == '':
            exit('State is empty')
        if symbol == '⊔':
            exit('Symbol is ⊔')


def check_Γ(Γ: set, Σ: set):
    """
    Exits the program if Γ is not valid
    :param Γ: Tape alphabet
    :param Σ: Input alphabet, assumed to be valid
    """
    if type(Γ) is not set:
        exit('Γ is not set')
    for symbol in Γ:
        if type(symbol) is not str:
            exit(f'Symbol is not str (found: {type(symbol)})')
        if symbol == '':
            exit('Symbol is empty')
    if '⊔' not in Γ:
        exit('Γ does not contain ⊔')
    if not Σ.issubset(Γ):
        exit('Σ is not subset of Γ')


def check_δ(δ: dict, Q: set, Γ: set, q_accept: str, q_reject: str):
    """
    Exits the program if Γ is not valid
    :param δ: Transition function
    :param Q: Set of states, assumed to be valid
    :param Γ: Tape alphabet, assumed to be valid
    :param q_accept: Accepting state, assumed to be valid
    :param q_reject: Rejecting state, assumed to be valid
    """
    if type(δ) is not dict:
        exit('δ is not dict')

    full_domain = domain(Q, Γ, q_accept, q_reject)
    full_codomain = codomain(Γ, Q)
    my_domain = set()
    my_codomain = set()
    for symbol in δ:
        for state in δ[symbol]:
            my_domain.add((symbol, state))
            my_codomain.add(δ[symbol][state])

    domain_difference = my_domain.difference(full_domain)
    codomain_difference = my_codomain.difference(full_codomain)
    if len(domain_difference) > 0:
        print('δ has an invalid domain:')
        for item in domain_difference:
            print(f' {item}')
        print(f'Valid domain:')
        for item in full_domain:
            print(f' {item}')
        exit(1)
    if len(codomain_difference) > 0:
        print('δ has an invalid codomain:')
        for item in codomain_difference:
            print(f' {item}')
        print('Valid codomain:')
        for item in full_codomain:
            print(f' {item}')
        exit(1)


def check_w(w: str):
    """
    Exits the program if w is not valid
    :param w: Input string
    """
    if type(w) is not str:
        exit('w is not str')
