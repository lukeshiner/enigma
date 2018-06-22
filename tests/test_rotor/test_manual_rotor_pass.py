"""Test rotors work correctly without a controller."""

from .rotor_test import RotorTest


class TestFullRotorPassThroughManual(RotorTest):
    """Test rotors and reflectors work correctly with manual control."""

    def encode(self, keypress):
        """Return a character after encyphering with rotors and reflectors."""
        right_rotor_output = self.right_rotor.encode(keypress)
        print('In: {}'.format(keypress))
        print(keypress, right_rotor_output)
        middle_rotor_output = self.middle_rotor.encode(right_rotor_output)
        print(right_rotor_output, middle_rotor_output)
        left_rotor_output = self.left_rotor.encode(middle_rotor_output)
        print(middle_rotor_output, left_rotor_output)
        reflector_output = self.reflector.encode(left_rotor_output)
        print(left_rotor_output, reflector_output)
        left_rotor_output = self.left_rotor.encode(
            reflector_output, reverse=True)
        print(reflector_output, left_rotor_output)
        middle_rotor_output = self.middle_rotor.encode(
            left_rotor_output, reverse=True)
        print(left_rotor_output, middle_rotor_output)
        output = self.right_rotor.encode(middle_rotor_output, reverse=True)
        print(middle_rotor_output, output)
        print('Out: {}'.format(output))
        print
        return output

    def test_rotor_encoding_with_full_passthrough(self):
        """Test rotors and reflectors work correctly with manual control."""
        self.reflector = self.get_reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
        self.left_rotor = self.get_rotor(
            'EKMFLGDQVZNTOWYHXUSPAIBRCJ', position='A')
        self.middle_rotor = self.get_rotor(
            'AJDKSIRUXBLHWTMCQGZNPYFVOE', position='A')
        self.right_rotor = self.get_rotor(
            'BDFHJLCPRTXVZNYEIWGAKMUSQO', position='A')
        output = []
        self.right_rotor.rotate()
        output.append(self.encode('A'))
        self.right_rotor.rotate()
        output.append(self.encode('A'))
        self.right_rotor.rotate()
        output.append(self.encode('A'))
        assert ''.join(output) == 'BDZ'

    def test_rotor_encoding_with_full_passthrough_with_ring_setting(self):
        """Test rotors and reflectors work correctly with manual control."""
        self.reflector = self.get_reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
        self.left_rotor = self.get_rotor(
            'EKMFLGDQVZNTOWYHXUSPAIBRCJ', position='A')
        self.middle_rotor = self.get_rotor(
            'AJDKSIRUXBLHWTMCQGZNPYFVOE', position='A')
        self.right_rotor = self.get_rotor(
            'BDFHJLCPRTXVZNYEIWGAKMUSQO', position='A', ring_setting=2)
        output = []
        self.right_rotor.rotate()
        output.append(self.encode('A'))
        self.right_rotor.rotate()
        output.append(self.encode('A'))
        self.right_rotor.rotate()
        output.append(self.encode('A'))
        self.right_rotor.rotate()
        output.append(self.encode('A'))
        self.right_rotor.rotate()
        output.append(self.encode('A'))
        assert ''.join(output) == 'UBDZG'
