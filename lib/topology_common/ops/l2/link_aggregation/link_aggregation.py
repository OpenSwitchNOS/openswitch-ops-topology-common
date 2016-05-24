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

""" Link aggregation CLI functions for OpenSwitch nodes 
    This file is part of the Topology Modular Framework Common Code Library.
    This module is supported in:
    - Modular Topology objects that support vtysh
"""

def create_l3_lag(dut, interfaces, ip, lag_id, step):
    """ Configure L3 lag and interfaces using libvtysh

    Arguments:
    dut -- A modular framework dut object that supports the vty shell
    interfaces -- List of interfaces to be configure to lag
    ip_address -- IP address to configure on lag interface
    lag_id -- Lag identifier
    """

    step("Configuring L3 lag in {}".format(dut.identifier))
    with dut.libs.vtysh.ConfigInterfaceLag(lag_id) as ctx:
        ctx.ip_address(ip)
        ctx.no_shutdown()

    for interface in interfaces:
        with dut.libs.vtysh.ConfigInterface(interface) as ctx:
            ctx.no_shutdown()
            ctx.lag(lag_id)

    lacp_ops = dut.libs.vtysh.show_lacp_aggregates()
    lag_name = 'lag{}'.format(lag_id)
    lag_int = lacp_ops[lag_name]['interfaces']
    for int in interfaces:
        assert dut.ports[int] in lag_int, \
            'interface {} was not added to lag'.format(dut.port[int])

