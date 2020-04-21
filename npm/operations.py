from common import get
from colorama import Fore

registry_url = 'http://registry.npmjs.org/'


def get_times(dependency):
    """
    Get all time's releases from specify dependency
    :param dependency: dependency name
    :return: list of times (e.g., [('1.0.0', '2015-03-09T03:09:05.477Z'), ('1.1.0', '2015-11-21T03:09:53.766Z')]
    """
    try:
        times_raw = get(registry_url + dependency).json()
    except:
        print(Fore.RED + 'package `{0}´ not found.'.format(dependency))
        return

    times = []
    times_raw = times_raw['time']
    for time in times_raw:
        if time.__eq__('modified') or time.__eq__('created'):
            continue

        # e.g., ('1.0.0', 2015-03-09T03:09:05.477Z')
        times.append((time, times_raw[time]))

    return times