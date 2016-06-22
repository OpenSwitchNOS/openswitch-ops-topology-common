# -*- coding: utf-8 -*-

"""
Common functions for pysical interfaces
"""

from time import sleep


def wait_until_up(switch, portlbls):
    """
    Wait until the interface, as mapped by the given portlbl, is marked as up.

    :param switch: The switch node.
    :param str or list portlbls: Port label/s that is mapped to the interface/s
    :return: None if interface is brought-up. If not, an assertion is raised.
    """

    if not isinstance(portlbls, list):
            portlbls = [portlbls]

    for portlbl in portlbls:
        for i in range(30):
            status = switch.libs.vtysh.show_interface(portlbl)
            if status['interface_state'] == 'up':
                break
            sleep(1)
        else:
            assert False, (
                'Interface {}:{} never brought-up after '
                'waiting for 30 seconds'.format(
                    switch.identifier, portlbl
                )
            )
