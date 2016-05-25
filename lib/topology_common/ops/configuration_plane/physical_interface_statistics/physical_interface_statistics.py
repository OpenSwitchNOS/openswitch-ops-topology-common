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

""" Physical Interface Statistics CLI functions for OpenSwitch nodes

This file is part of the Topology Modular Framework Common Code Library.

This module is supported in:
    - Modular Topology objects that support vtysh
"""


def get_multi_interfaces_stats(node, interface_list, step):
    """ Get the information from the show interface <name> for multiple
    interfaces on a list using libvtysh.

    Arguments:
    node -- A modular framework node object that supports the vty shell.
    interface_list -- List of names of each interface that is going to be used.
                      Ex: ["1", "vlan1", "2", "lag2"]
    step -- A modular framework step object to set a mark for the test step.

    Returns:
    result -- Dictionary of all interfaces parameters returned by vtysh.
    """
    step('### Get interfaces statistics on ###'.format(node.alias))
    result = {}
    for int_id in interface_list:
        result[int_id] = node.libs.vtysh.show_interface(int_id)
    return result
