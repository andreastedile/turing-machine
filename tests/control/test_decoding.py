from unittest import TestCase

from ordered_set import OrderedSet as Set

from turing_machine.control.control import Control


class TestDecoding(TestCase):
    def test_rule_encoding(self):
        control = Control.from_encoding('01001000101001100010101001001100010010010100110001000100010010')
        δ = {
            ('q_1', '1'): ('q_3', '0', 'R'),
            ('q_3', '0'): ('q_1', '1', 'R'),
            ('q_3', '1'): ('q_2', '0', 'R'),
            ('q_3', 'B'): ('q_3', '1', 'L')
        }

        self.assertEqual(Set(['q_1', 'q_2', 'q_3']), control.Q)
        self.assertEqual(Set(['0', '1']), control.Σ)
        self.assertEqual(Set(['0', '1', 'B']), control.Γ)
        self.assertEqual(δ, control._δ)
        self.assertEqual('q_1', control.q_0)
        self.assertEqual('B', control.B)
        self.assertEqual(Set(['q_2']), control.F)
