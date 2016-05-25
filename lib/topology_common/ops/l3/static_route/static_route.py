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

""" Static Routes CLI functions for OpenSwitch nodes

This file is part of the Topology Modular Framework Common Code Library.

This module is supported in:
    - Modular Topology objects that support vtysh
"""


def create_increment_next_hops_on_static_route(node, network,
                                               nexthop_init_1oct,
                                               nexthop_final_1oct,
                                               nexthop_4oct, step,
                                               nexthop_step_1oct=1):
    """ Create multiples next-hops for a single static route using libvtysh.
    The function increments the first octet of the next-hop ip address and uses
    the same last octet for all next-hops.

    Arguments:
    node -- A modular framework node object that supports the vty shell.
    network -- Network that will be configured. Ex:'100.0.0.0/24'.
    nexthop_init_1oct -- Initial value for the next-hop's first octet.
                         Integer(1-255).
    nexthop_final_1oct -- Final value for the next-hop's first octet.
                          Integer(1-255).
    nexthop_step_1oct -- Incremental step for the next-hop's first octet.
                         Integer.
    nexthop_4oct -- Host number for the next-hop. Integer(1-255).
    step -- A modular framework step object to set a mark for the test step.
    """
    step("### Configure next-hops for a Static Route on {} ###".format(
        node.alias))
    # Configure static routing for each next-hop
    with node.libs.vtysh.Configure() as ctx:
        for nh in range(nexthop_init_1oct, nexthop_final_1oct + 1,
                        nexthop_step_1oct):
            next_hop = ('{}.0.0.{}'.format(nh, nexthop_4oct))
            ctx.ip_route(network, next_hop, '1')


def assert_next_hops_on_single_static_route_(node, num_routes, network,
                                             nexthop_init_1oct,
                                             nexthop_final_1oct,
                                             nexthop_step_1oct, nexthop_4oct,
                                             step):
    """ Assert that multiples next-hops for a single static route are displayed
    on a the show ip route output using libvtysh.

    Arguments:
    node -- A modular framework node object that supports the vty shell.
    num_routes -- Number of routes expected on the output. Type: Integer.
    network -- Network that will be verified for next-hops. Ex:'100.0.0.0/24'.
    nexthop_init_1oct -- Initial value for the next-hop first octet.
                         Type: Integer(1-255).
    nexthop_final_1oct -- Final value for the next-hop first octet.
                          Type: Integer(1-255).
    nexthop_step_1oct -- Incremental step for the next-hop first octet.
                         Type: Integer.
    nexthop_4oct -- Host number for the next-hop. Type: Integer(1-255).
    step -- A modular framework step object to set a mark for the test step.
    """
    step("### Verify that all routes are displayed on {} ###".format(
        node.alias))

    routes = node.libs.vtysh.show_ip_route()

    # Check that the amount of routes equals the expected value
    assert len(routes) == num_routes, \
        'ERROR: Number of routes on {} is not as expected'.format(node.alias)

    # Check that each next hop is advertised on the routing table on the switch
    count = 0
    next_hops_num = 0
    for item in routes:
        if item['id'] == network:
            for nh in range(nexthop_init_1oct, nexthop_final_1oct + 1,
                            nexthop_step_1oct):
                next_hops_num = next_hops_num + 1
                for next_hop in item['next_hops']:
                    if next_hop["via"] == ('{}.0.0.{}'.format(nh + 10,
                                                              nexthop_4oct)):
                        count = count + 1
    assert count == next_hops_num,  \
        ('ERROR: Not all next hops are advertised in the routing table on ',
         '{}'.format(node.alias))
