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

""" ECMP CLI functions for OpenSwitch nodes

This file is part of the Topology Modular Framework Common Code Library.

This module is supported in:
    - Modular Topology objects that support vtysh
"""


def assert_ecmp_default(node, step):
    """ Assert ECMP default configuration using libvtysh

    Arguments:
    node -- A modular framework node object that supports the vty shell
    step -- A modular framework step object to set a mark for the test step
    """
    step("### Verify ECMP configuration on {} ###".format(node.alias))
    ecmp_config_dut = node.libs.vtysh.show_ip_ecmp()

    # Check if the feature is enabled by default on switch
    assert ecmp_config_dut["global_status"], \
        'ERROR: ECMP is not enabled by default'
    assert ecmp_config_dut["src_ip"], \
        'ERROR: ECMP source IP is not enabled by default'
    assert ecmp_config_dut["dest_ip"], \
        'ERROR: ECMP destination IP is not enabled by default'
    assert ecmp_config_dut["src_port"], \
        'ERROR: ECMP source port is not enabled by default'
    assert ecmp_config_dut["dest_port"], \
        'ERROR: ECMP destination port is not enabled by default'
    assert ecmp_config_dut["resilient"], \
        'ERROR: ECMP resilient hashing is not enabled by default'
