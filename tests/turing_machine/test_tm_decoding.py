from unittest import TestCase

from turing_machine.turing_machine.turing_machine import TuringMachine as TM


class TestTuringMachine(TestCase):
    def setUp(self) -> None:
        self.M = TM.from_encoding('01001000101001100010101001001100010010010100110001000100010010')

    def test_resume(self):
        self.M.place_input('1100')

        try:
            while True:
                next(self.M)
        except StopIteration as si_:
            si = si_

        self.assertIsInstance(si, StopIteration)
        self.assertEqual(str(si), 'Accept')
