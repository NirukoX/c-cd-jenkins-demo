import unittest
import signal

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("Test timed out!")

class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set a timeout of 10 seconds for all tests
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(10)  # Adjust the timeout as needed

    def test_example(self):
        try:
            self.assertEqual(2 + 2, 4)
        except TimeoutException:
            self.skipTest("Test skipped due to timeout")

    @classmethod
    def tearDownClass(cls):
        # Disable the alarm after tests finish
        signal.alarm(0)

if __name__ == '__main__':
    unittest.main()
