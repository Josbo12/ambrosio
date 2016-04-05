import unittest
from ambrosio import commandlist

class TestCommandList(unittest.TestCase)

    def test_000_newqueue_length(self):
        c1 = commandlist.Commandlist()
        self.assertEqual(cl.length(),0)


    def test_001_newqueue_cantpop(self):
        c1 = commandlist.Commandlist()
        self.assertRaises(IndexError,c1.next)

    def test_002_push_then_pop(self):
        c1 = commandlist.Commandlist()
        c1.append("Test")
        c = c1.next()
        self.assertEqual(c,"Test")
