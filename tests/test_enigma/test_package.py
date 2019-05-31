"""Test the enigma package."""

import unittest

from enigma import __version__


class TestPackage(unittest.TestCase):
    """Test the enigma package."""

    def test_version_file_attributes(self):
        """Test the __version__ file has the necessary attributes."""
        self.assertTrue(hasattr(__version__, "__title__"))
        self.assertTrue(hasattr(__version__, "__description__"))
        self.assertTrue(hasattr(__version__, "__url__"))
        self.assertTrue(hasattr(__version__, "__version__"))
        self.assertTrue(hasattr(__version__, "__author__"))
        self.assertTrue(hasattr(__version__, "__author_email__"))
        self.assertTrue(hasattr(__version__, "__license__"))
        self.assertTrue(hasattr(__version__, "__copyright__"))
