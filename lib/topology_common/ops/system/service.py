# -*- coding: utf-8 -*-

""" SystemD Service Management functions for OpenSwitch nodes

This file is part of the Topology Modular Framework Common Code Library.
It uses systemd (systemctl), the default service manager in OpenSwitch.

This module is not supported in:
    - Modular Topology objects that do not support the Bash shell
    - Systems that do not use systemd as its service manager
"""


def is_running(node, service):
    """ Uses systemctl to verify that a service is running

    Return type is Boolean.

    Arguments:
    node -- A modular framework node object that supports the Bash shell
    service -- The name of the service
    """
    output = node("systemctl status {service}".format(**locals()),
                  shell='bash')
    # Expected output of systemctl status is similar to:
    #
    # bash-4.3# systemctl status ops-sysd
    # ops-sysd.service - OpenSwitch System Daemon (ops-sysd)
    # Loaded: loaded (/lib/systemd/system/ops-sysd.service; enabled;)
    # Active: active (running) since Fri 2016-04-01 17:35:27 UTC; 11min ago
    # Process: ... (here more info)
    lines = output.split('\n')
    return "active (running)" in (lines[2] if len(lines) > 2 else "")


def get_pid(node, service):
    """ Uses systemctl to obtain the PID of a running service

    Return type is Integer.
    Returns 0 for a service that does not exist or is not running.

    Arguments:
    node -- A modular framework node object that supports the Bash shell
    service -- The name of the service
    """
    output = node("systemctl show {service} "
                  "--property=MainPID | cat".format(**locals()),
                  shell="bash")
    # Expected output of systemctl status is similar to the following.
    # For a not running or unexisting service, the output is MainPID=0
    #
    # bash-4.3# systemctl show ops-sysd --property=MainPID | cat
    # MainPID=1760
    lines = output.split('=')
    return int(lines[1]) if len(lines) > 1 else 0


def restart(node, service):
    """ Runs systemctl restart on a service. The result is not checked.

    Arguments:
    node -- A modular framework node object that supports the Bash shell
    service -- The name of the service
    """
    node("systemctl restart {service}".format(**locals()), shell='bash')
