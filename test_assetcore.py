# test_assetcore.py
"""
Tests for AssetCore module.
"""

import unittest
from assetcore import AssetCore

class TestAssetCore(unittest.TestCase):
    """Test cases for AssetCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AssetCore()
        self.assertIsInstance(instance, AssetCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AssetCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
