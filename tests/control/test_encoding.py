from unittest import TestCase

from ordered_set import OrderedSet as Set

from turing_machine.control.control import Control

# See Hopcroft, ch. 9.1

Q = Set(['q1', 'q2', 'q3'])
Σ = Set(['0', '1'])
Γ = Set(['0', '1', 'B'])
δ = {
    ('q1', '1'): ('q3', '0', 'R'),
    ('q3', '0'): ('q1', '1', 'R'),
    ('q3', '1'): ('q2', '0', 'R'),
    ('q3', 'B'): ('q3', '1', 'L')
}


class TestEncoding(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.control = Control(Q, Σ, Γ, δ, 'q1', 'B', Set(['q2']))

    def test_rule_encoding(self):
        self.assertEqual('0100100010100', self.control.encode_rule('q1', '1', 'q3', '0', 'R'))
        self.assertEqual('0001010100100', self.control.encode_rule('q3', '0', 'q1', '1', 'R'))
        self.assertEqual('00010010010100', self.control.encode_rule('q3', '1', 'q2', '0', 'R'))
        self.assertEqual('0001000100010010', self.control.encode_rule('q3', 'B', 'q3', '1', 'L'))
