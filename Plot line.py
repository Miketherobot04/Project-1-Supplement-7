def plot_line(y_intercept, slope, lower_x, upper_x):
    """
    Plots a line given the y-intercept, slope, and x boundaries.
    
    Parameters:
    y_intercept (float): The y-intercept of the line.
    slope (float): The slope of the line.
    lower_x (float): The lower boundary of the x-axis.
    upper_x (float): The upper boundary of the x-axis.
    """
    x = np.linspace(lower_x, upper_x, 100)
    y = slope * x + y_intercept
    plt.plot(x, y, label=f"y = {slope}x + {y_intercept}", color='red')
    plt.xlim(lower_x, upper_x)
    plt.title("Line Plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.legend()
    plt.show()