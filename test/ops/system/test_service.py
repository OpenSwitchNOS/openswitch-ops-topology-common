# Copyright (C) 2016 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


""" Test suite for the SystemD Service Management module """

import pytest  # noqa
from topology_common.ops.system.service import get_pid, is_running


def systemctl_status_cmd(cmd, shell="bash"):
    """ Returns the output that systemctl status <service> would return

    This is a stub function. The output corresponds to a running service.
    The expected usage of this function is to replace a Node object which
    is able to run CLI commands.

    This function ignores the input params and returns the normal output of
    systemctl which is similar to:

        bash-4.3# systemctl status ops-sysd
          ops-sysd.service - OpenSwitch System Daemon (ops-sysd)
           Loaded: loaded (/lib/systemd/system/ops-sysd.service; enabled;
           Active: active (running) since Fri 2016-04-01 17:53:00 UTC; 1h
          Process: 1759 ExecStart=/sbin/ip netns exec nonet /usr/bin/ops-sysd
          Process: 1758 ExecStartPre=/bin/rm -f /var/run/openvswitch/
         Main PID: 1760 (ops-sysd)
           Memory: 2.3M
           CGroup: /system.slice/ops-sysd.service
    """
    return (
        '  ops-sysd.service - OpenSwitch System Daemon (ops-sysd)\n'
        '   Loaded: loaded (/lib/systemd/system/ops-sysd.service; enabled\n'
        '   Active: active (running) since Fri 2016-04-01 17:53:00 UTC; ...\n'
        '  Process: 1759 ExecStart=/sbin/ip netns exec nonet /usr/bin/  ...\n'
        '  Process: 1758 ExecStartPre=/bin/rm -f /var/run/openvswitch/  ...\n'
        ' Main PID: 1760 (ops-sysd)\n'
        '   Memory: 2.3M\n'
        '   CGroup: /system.slice/ops-sysd.service\n')


def systemctl_show_pid_cmd(cmd, shell="bash"):
    """ Returns the output that systemctl show <service> would return

    This is a stub function.
    The expected usage of this function is to replace a Node object which
    is able to run CLI commands.

    The command being run is:

        systemctl show {service} --property=MainPID | cat

    And the value returned is:

        MainPID=1790

    This function ignores the input params and returns the normal output of
    systemctl which is similar to:

    For a running process:
        bash-4.3# systemctl show ops-sysd --property=MainPID | cat
        MainPID=1790
    """
    return ('MainPID=1790')


def setup_module(module):
    pass


def teardown_module(module):
    pass


def test_is_running():
    """ Tests the service.is_running() function

    Uses the stub systemctl_status_cmd defined above
    """
    assert is_running(systemctl_status_cmd, "ops-test") is True, \
        "Did not return True for a running process"


def test_get_pid():
    """ Tests the service.get_pid() function

    Uses the stub systemctl_show_pid_cmd defined above
    """
    assert get_pid(systemctl_show_pid_cmd, "ops-test") == 1790, \
        "Did not return expected PID"
