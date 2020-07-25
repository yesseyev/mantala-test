import unittest

from answer import TwitterParser


class TwitterParserTest(unittest.TestCase):
    def setUp(self) -> None:
        self.twitter_parser = TwitterParser()

    def tearDown(self) -> None:
        self.twitter_parser.quit_browser()
        pass

    def test_kmbappe(self):
        """ At the moment of writing test @KMbappe had 4.5M followers """
        followers = self.twitter_parser.get_followers_count('https://twitter.com/KMbappe')
        self.assertGreater(followers, 4_000_000)
        self.assertLess(followers, 6_000_000)

    def test_kobebryant(self):
        """ At the moment of writing test @kobebryant had 15.4M followers """
        followers = self.twitter_parser.get_followers_count('https://twitter.com/kobebryant')
        self.assertGreater(followers, 15_000_000)
        self.assertLess(followers, 17_000_000)

    def test_low_speed_trump(self):
        """ At the moment of writing test @realDonaldTrump had 84.1M followers """
        # Setting 100 kb/s throughput for bot upload and download
        self.twitter_parser.set_network_conditions(
            offline=False,
            latency=5,  # additional latency (ms)
            download_throughput=100 * 1024,  # maximal throughput
            upload_throughput=100 * 1024)  # maximal throughput

        followers = self.twitter_parser.get_followers_count('https://twitter.com/realDonaldTrump')
        self.assertGreater(followers, 80_000_000)
        self.assertLess(followers, 90_000_000)

    def test_non_existing(self):
        """ At the moment of writing test @towofff does not exist """
        followers = self.twitter_parser.get_followers_count('https://twitter.com/towofff')
        self.assertEqual(followers, -1)

    def test_non_profile_page(self):
        with self.assertRaises(ValueError):
            self.twitter_parser.get_followers_count('http://t.me/test_fail')
        pass


if __name__ == '__main__':
    unittest.main()
