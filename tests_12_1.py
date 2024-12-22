import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walk = runner.Runner('Аршин')
        for i in range(10):
            walk.walk()
        self.assertEqual(walk.distance, 50)

    def test_run(self):
        run = runner.Runner('Би')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        walk2 = runner.Runner('Вио')
        run2 = runner.Runner('Галл')
        for i in range(10):
            walk2.walk()
            run2.run()
        self.assertNotEqual(run2.distance, walk2.distance)
