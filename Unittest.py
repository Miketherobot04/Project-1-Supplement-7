import unittest

class TestPlotFunctions(unittest.TestCase):
    
    def test_normal_distribution(self):
        """
        Tests if plot_normal_distribution runs without errors.
        """
        try:
            plot_normal_distribution()
        except Exception as e:
            self.fail(f"plot_normal_distribution() raised an exception: {e}")
    
    def test_line_plot(self):
        """
        Tests if plot_line works correctly with valid input.
        """
        try:
            plot_line(0, 1, -10, 10)  # Simple y = x line
        except Exception as e:
            self.fail(f"plot_line() raised an exception: {e}")
    
    def test_live_plot(self):
        """
        Tests live_point_plot by passing a valid distribution function.
        """
        try:
            live_point_plot(lambda: np.random.normal(loc=0, scale=1))
        except Exception as e:
            self.fail(f"live_point_plot() raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()