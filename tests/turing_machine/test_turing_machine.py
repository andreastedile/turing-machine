from unittest import TestCase

from ordered_set import OrderedSet as Set

from turing_machine.turing_machine.turing_machine import TuringMachine as TM

Q = Set(['q_0', 'q_1', 'q_2', 'q_3', 'q_4'])
Σ = Set(['0', '1'])
Γ = Set(['0', '1', 'X', 'Y', 'B'])
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


class TestTuringMachine(TestCase):
    def setUp(self) -> None:
        self.M = TM(Q, Σ, Γ, δ, 'q_0', 'B', Set(['q_4']))

    def test_resume(self):
        self.M.resume(['X', 'X', 'q_0', 'Y', 'Y'])

        try:
            while True:
                next(self.M)
        except StopIteration as si_:
            si = si_

        self.assertIsInstance(si, StopIteration)
        self.assertEqual(str(si), 'Accept')

    def test_resume_extra_state(self):
        with self.assertRaises(AssertionError):
            self.M.resume(['X', 'X', 'q_0', 'Y', 'q_0', 'Y', ])

    def test_resume_unknown_symbol(self):
        with self.assertRaises(AssertionError):
            self.M.resume(['X', 'X', 'q_0', 'Y', 'foo', 'Y', ])
