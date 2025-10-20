# test_sandutility.py
"""
Tests for SandUtility module.
"""

import unittest
from sandutility import SandUtility

class TestSandUtility(unittest.TestCase):
    """Test cases for SandUtility class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SandUtility()
        self.assertIsInstance(instance, SandUtility)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SandUtility()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
