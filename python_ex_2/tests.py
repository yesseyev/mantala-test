import unittest

from answer import RandomLottery


class LotteryTest(unittest.TestCase):
    def test_result_length(self):
        lottery = RandomLottery(number_of_picks=10)
        lottery.run_lottery()
        result = lottery.get_result()

        # Picks number test
        self.assertEqual(len(result), 10)

    def test_output_sort(self):
        lottery = RandomLottery(number_of_balls=100, number_of_picks=10)
        lottery.run_lottery()
        result = lottery.get_result()

        # Checking ascending order
        self.assertEqual(result, sorted(result))

    def test_failure_picks(self):
        with self.assertRaises(ValueError):
            lottery = RandomLottery(number_of_balls=50, number_of_picks=100)

    def test_failure_zero(self):
        with self.assertRaises(ValueError):
            lottery = RandomLottery(number_of_balls=0, number_of_picks=10)

    def test_failure_negative(self):
        with self.assertRaises(ValueError):
            lottery = RandomLottery(number_of_balls=50, number_of_picks=-10)

    def test_failure_second_run(self):
        lottery = RandomLottery(number_of_balls=50, number_of_picks=10)
        lottery.run_lottery()

        with self.assertRaises(RuntimeError):
            lottery.run_lottery()  # Cannot run second time on picked set


if __name__ == '__main__':
    unittest.main()
