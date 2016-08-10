# Copyright (C) 2016 Hewlett Packard Enterprise Development LP
# All Rights Reserved.
#
# The contents of this software are proprietary and confidential
# to the Hewlett Packard Enterprise Development LP. No part of this
# program may be photocopied, reproduced, or translated into another
# programming language without prior written consent of the
# Hewlett Packard Enterprise Development LP.

"""
REST functions for OpenSwitch nodes

This file is part of the Topology Modular Framework Common Code Library.

This module is supported in:
    - Modular Topology objects that support vtysh
"""

ORIGIN_FILE = '/etc/ssl/certs/server.crt'
REMOTE_SIDE = 'destination'


def create_certificate_and_copy_to_host(
        node,
        switch_ip,
        remote_ip,
        key_size='1024',
        destination_file='/usr/local/share/ca-certificates/server.crt',
        remote_user='root',
        remote_pass='procurve',
        step=None
):

    """
    Create a new certificate in the switch and copy it to a host

    :param node: A modular framework DUT object that supports the vty shell
    :param step: A modular framework step object to set a mark for the test
    :param str switch_ip: The IP address of the switch
    :param str key_size: The key size of the certificate, default 1024
    :param str destination_file: Path of the file in the destination device
    :param str remote_user: Remote host username. Default is 'root'
    :param str remote_ip: The IP address of the remote host
    :param str remote_pass: Remote host password. Default is 'procurve'
    """
    step and step('Generate new certificate with size of {}, \
                   and copy it from {} to {}'.format(key_size, ORIGIN_FILE,
                                                     destination_file))

    node.libs.openssl.generate_rsa_key(switch_ip=switch_ip,
                                       key_size=key_size)

    node.libs.files_management.scp_command(ORIGIN_FILE,
                                           destination_file,
                                           remote_user, remote_ip,
                                           REMOTE_SIDE, remote_pass)
