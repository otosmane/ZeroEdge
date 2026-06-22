# test_zeroedge.py
"""
Tests for ZeroEdge module.
"""

import unittest
from zeroedge import ZeroEdge

class TestZeroEdge(unittest.TestCase):
    """Test cases for ZeroEdge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZeroEdge()
        self.assertIsInstance(instance, ZeroEdge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZeroEdge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
