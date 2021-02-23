from unittest import TestCase

from turing_machine.tape.tape import Tape


class TestTape(TestCase):
    def test_get_item(self):
        tape = Tape('B')
        tape[-1]
        tape[0]
        tape.append('foo')
        tape[1]

    def test_set_item(self):
        tape = Tape('B')
        tape[-1] = 'foo'
        tape[0] = 'fee'
        tape[1] = 'bar'
