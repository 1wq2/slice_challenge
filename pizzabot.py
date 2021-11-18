import sys
import re


class Pizzabot:
    """ Delivery bot

    Contains data about location, destination addresses, path, and
    methods to operate on that data.
    """
    def __init__(self, coords):
        """
        loc: current location of the bot
        :param coords: coordinates of the delivery destinations
        trace: path/instructions for the bot to take
        """
        self.loc = [0, 0]
        self.coords = coords
        self.trace = ""

    def update_loc(self, point):
        """
        Calculates distance between bot's location(self.loc)
        and the next delivery address(point), updates bot's location,
        prepares step info - distance between
        bot's location and the current delivery address

        :param point: current delivery address
        """

        step = list(map(lambda x, y: x - y, point, self.loc))
        self.loc = point

        self.update_trace(step)

    def update_trace(self, step):
        """
        Updates bot's path. X axis aligns first, Y axis updates next.

        :param step: distance between bot's location and the current delivery address
        """

        if step[0] < 0:
            self.trace += 'W' * abs(step[0])
        else:
            self.trace += 'E' * step[0]
        if step[1] < 0:
            self.trace += 'S' * abs(step[1])
        else:
            self.trace += 'N' * step[1]

        self.trace += 'D'


def get_route(coords):
    """
    Initializes Pizzabot, iterates over destinations' coordinates,
    prepares data for the point - current delivery address

    :param coords:
    :return: trace - bot's instructions
    """
    bot1 = Pizzabot(coords)

    for i in range(0, len(coords), 2):
        point = coords[i:i + 2]
        if point == [0, 0]:
            bot1.trace = 'D'
        # We won't deliver('D') to the same location twice,
        # if the bot hasn't moved(a situation, where next destination is the same
        # as the current one)
        if bot1.loc != point:
            bot1.update_loc(point)

    print(bot1.trace)
    return bot1.trace


def parser(args):
    """
    Works on user's input. Insures, that only the correct input
    will later be processed by the bot.

    :param args: user's input
    :return: coords - delivery location data
    """

    # this check will be useful in a situation, where one axis is missing for some reason
    if '(' not in args:
        raise ValueError('Use bracket "(" to delimit coords values from the grid ones')

    if len(re.findall("\d+\.\d+", args)) != 0:
        raise ValueError('No floats allowed for this grid')

    num_input = list(map(int, re.compile('-?\d+').findall(args)))

    grid_size = [int(x) for x in args.split('(', 1)[0] if x.isdigit()]

    if len(grid_size) != 2:
        raise ValueError('Grid input needs 2 values')
    if any(x < 1 for x in grid_size):
        raise ValueError('Provide positive integers for a grid size')

    coords = num_input[2:]

    if any(x < 0 for x in coords):
        raise ValueError('Provide non-negative integers for coordinates')
    if len(coords) < 2:
        raise ValueError('At least one point should be provided as destination')
    if len(coords) % 2 != 0:
        raise ValueError('Each point must have 2 coordinates')
    if max(grid_size) < max(coords):
        raise ValueError('Coord value cannot exceed the grid size')

    return coords


if __name__ == '__main__':
    try:
        crds = parser(sys.argv[1])
        get_route(crds)
    except IndexError:
        print('Please provide correct input arguments. Example: python3 ./pizzabot.py "5x5 (1, 3) (4, 4)"')
        sys.exit(1)


