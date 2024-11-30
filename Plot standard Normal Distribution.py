def plot_normal_distribution():
    """
    Plots 200 points sampled from a standard normal distribution.
    """
    data = np.random.normal(loc=0, scale=1, size=200)
    plt.scatter(range(len(data)), data, color='blue', alpha=0.6)
    plt.title("Standard Normal Distribution (200 points)")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid()
    plt.show()