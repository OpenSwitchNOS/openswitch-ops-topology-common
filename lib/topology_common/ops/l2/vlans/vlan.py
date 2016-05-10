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
