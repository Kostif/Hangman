import unittest
import hangman

class TestHangman(unittest.TestCase):

    def test_win_check(self):
        guessed_word = 'test'
        current_word = 'test'
        self.assertTrue(hangman.win_check(guessed_word,current_word))

    
if __name__ == '__main__':
    unittest.main()