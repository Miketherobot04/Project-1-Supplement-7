def live_point_plot(distribution_function):
    """
    Generates one point every second following the given distribution and updates the graph.
    Only the 10 most recent points are shown.
    
    Parameters:
    distribution_function (callable): A function that generates a random point.
    """
    fig, ax = plt.subplots()
    points = []

    def update(frame):
        nonlocal points
        new_point = distribution_function()
        points.append(new_point)
        if len(points) > 10:
            points.pop(0)
        ax.clear()
        ax.plot(range(len(points)), points, marker='o', color='green')
        ax.set_xlim(0, 10)
        ax.set_ylim(-5, 5)
        ax.set_title("Live Point Plot")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Value")
        ax.grid()

    ani = FuncAnimation(fig, update, interval=1000)
    plt.show()