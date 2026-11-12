import unittest
import numpy as np
from simulations.models import monty_hall, estimate_pi, expected_value, ant

class ModelsTest(unittest.TestCase):
    def test_monty_hall_complement_and_limit(self):
        _, stay, switch = monty_hall(100000)
        np.testing.assert_allclose(stay + switch, 1)
        self.assertAlmostEqual(switch[-1], 2/3, delta=0.01)
    def test_pi_and_expectation(self):
        self.assertAlmostEqual(estimate_pi(100000)[2][-1], np.pi, delta=0.03)
        self.assertAlmostEqual(expected_value(100000)[-1], 3.5, delta=0.03)
    def test_first_ant_step_and_determinism(self):
        self.assertEqual(ant(1), {(0, 0): 1})
        self.assertEqual(ant(100), ant(100))
        self.assertTrue(all(0 <= c < 7 for c in ant(100, True).values()))

if __name__ == "__main__": unittest.main()
