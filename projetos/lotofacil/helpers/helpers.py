from screeninfo import get_monitors

def get_width_height_monitor(monitor=0):
    """
        Retorna as dimensões, como tupla, do monitor.
        Returns the dimensions, as tuple, the monitor.
    """

    try:
        monitor = get_monitors()[monitor]
        return (monitor.width, monitor.height)
    except (TypeError, IndexError):
        print('Invalid option. Selected monitor does not exist.')
        return False

