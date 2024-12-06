import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import pytest for writing the tests
import pytest
# Import the module to be tested
from calculator import ask_question, play_game
# Import mock to mock dependencies
from unittest.mock import patch, MagicMock

# Test the ask_question function
class TestAskQuestion:
    @patch('calculator.random.randint')
    @patch('calculator.random.choice')
    def test_ask_question_addition(self, mock_choice, mock_randint):
        """
        Test asking an addition question.
        """
        mock_randint.side_effect = [3, 5]  # Mocking randint to return 3 and 5
        mock_choice.return_value = '+'  # Mocking choice to return '+'
        question, answer = ask_question()
        assert question == "What is 3 + 5?"
        assert answer == 8

    @patch('calculator.random.randint')
    @patch('calculator.random.choice')
    def test_ask_question_division(self, mock_choice, mock_randint):
        """
        Test asking a division question, ensuring no division by zero occurs.
        """
        mock_randint.side_effect = [8, 2]  # Mocking randint to return 8 and 2
        mock_choice.return_value = '/'  # Mocking choice to return '/'
        question, answer = ask_question()
        assert question == "What is 8 / 2?"
        assert answer == 4.0

# Test the play_game function
class TestPlayGame:
    @patch('calculator.ask_question')
    @patch('calculator.input', create=True)
    @patch('calculator.time.time')
    def test_play_game_success(self, mock_time, mock_input, mock_ask_question):
        """
        Test playing the game successfully by correctly answering a question.
        """
        mock_time.side_effect = [0, 0, 1]  # Mocking time to simulate game duration
        mock_input.return_value = '8'  # Mocking user input to return '8'
        mock_ask_question.return_value = ("What is 3 + 5?", 8)  # Mocking ask_question to return a predefined question and answer
        with patch('builtins.print') as mock_print:
            play_game()
            mock_print.assert_any_call("Correct! Your score is:", 1)

    @patch('calculator.ask_question')
    @patch('calculator.input', create=True)
    @patch('calculator.time.time')
    def test_play_game_timeout(self, mock_time, mock_input, mock_ask_question):
        """
        Test game ending due to timeout.
        """
        mock_time.side_effect = [0, 31]  # Mocking time to simulate game duration exceeded
        with patch('builtins.print') as mock_print:
            play_game()
            mock_print.assert_any_call("\nTime's up! You scored 0 points!")

    @patch('calculator.ask_question')
    @patch('calculator.input', create=True)
    @patch('calculator.time.time')
    def test_play_game_incorrect_answer(self, mock_time, mock_input, mock_ask_question):
        """
        Test playing the game and answering a question incorrectly.
        """
        mock_time.side_effect = [0, 0, 1]  # Mocking time to simulate game duration
        mock_input.return_value = '3'  # Mocking user input to return '3'
        mock_ask_question.return_value = ("What is 3 + 5?", 8)  # Mocking ask_question to return a predefined question and answer
        with patch('builtins.print') as mock_print:
            play_game()
            mock_print.assert_any_call("Wrong! The correct answer was 8.")
            mock_print.assert_any_call("Game Over! Your final score is 0.")

    @patch('calculator.ask_question')
    @patch('calculator.input', create=True)
    @patch('calculator.time.time')
    def test_play_game_invalid_input(self, mock_time, mock_input, mock_ask_question):
        """
        Test playing the game with an invalid input.
        """
        mock_time.side_effect = [0, 0, 1]  # Mocking time to simulate game duration
        mock_input.side_effect = ['not a number', '8']  # Mocking user input to first return an invalid input then '8'
        mock_ask_question.return_value = ("What is 3 + 5?", 8)  # Mocking ask_question to return a predefined question and answer
        with patch('builtins.print') as mock_print:
            play_game()
            mock_print.assert_any_call("Invalid input! Please enter a number.")