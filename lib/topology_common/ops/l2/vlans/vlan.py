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


""" VLAN CLI functions for OpenSwitch nodes

This file is part of the Topology Modular Framework Common Code Library.

This module is supported in:
    - Modular Topology objects that support vtysh
"""


def create_vlan_interface(node, vlan_id, ip_address):
    """ Configure VLAN interface using libvtysh

    Arguments:
    node -- A modular framework node object that supports the vty shell
    vlan_id -- VLAN ID for interface to be configured
    ip_address -- IP address to configure on interface
    """

    with node.libs.vtysh.ConfigVlan(vlan_id) as ctx:
        ctx.no_shutdown()

    with node.libs.vtysh.ConfigInterfaceVlan(vlan_id) as ctx:
        ctx.ip_address(ip_address)
        ctx.no_shutdown()
