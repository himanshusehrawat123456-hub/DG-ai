"""
DG AI Version 1
Memory System Testing

Purpose:
- Test memory operations
- Check storing and retrieving data

Version: 1.0
"""


import unittest



class TestMemory(unittest.TestCase):
    """
    Test DG AI Memory System.
    """



    def setUp(self):
        """
        Create test memory.
        """

        self.memory = {}



    def test_store_memory(self):
        """
        Test saving memory.
        """

        self.memory["name"] = "Himanshu"


        self.assertEqual(
            self.memory["name"],
            "Himanshu"
        )



    def test_get_memory(self):
        """
        Test retrieving memory.
        """

        self.memory["language"] = "Python"


        result = self.memory.get(
            "language"
        )


        self.assertEqual(
            result,
            "Python"
        )



    def test_clear_memory(self):
        """
        Test clearing memory.
        """

        self.memory["data"] = "test"


        self.memory.clear()


        self.assertEqual(
            len(self.memory),
            0
        )




if __name__ == "__main__":

    unittest.main()
