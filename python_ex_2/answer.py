import heapq
import random


class RandomLottery:
    def __init__(self, number_of_balls=50, number_of_picks=10):
        # Handling exceptions
        if number_of_balls <= 0 or number_of_picks <= 0:
            raise ValueError('Number of balls and number of picks must be greater than 0')
        elif number_of_balls < number_of_picks:
            raise ValueError('Number of picks cannot exceed number of balls')

        # Setting values
        self._number_of_balls = number_of_balls
        self._number_of_picks = number_of_picks

        self.__balls = [False] * self._number_of_balls  # Range between 0 to N-1
        self.__heap = []  # Heap for holding balls
        self.__result = []

        random.seed()  # Randomizing

    def __pick_ball(self):
        ball_idx = random.randrange(self._number_of_balls)

        while self.__balls[ball_idx]:  # Checking if ball was picked
            ball_idx = random.randrange(self._number_of_balls)

        self.__balls[ball_idx] = True  # Marking ball as picked

        return ball_idx

    def run_lottery(self):
        if len(self.__result) > 0:
            raise RuntimeError('Lottery already run.')

        for i in range(self._number_of_picks):
            ball_idx = self.__pick_ball()
            heapq.heappush(self.__heap, ball_idx)

        self.__result = [(heapq.heappop(self.__heap) + 1) for i in range(self._number_of_picks)]

    def get_result(self):
        return self.__result
