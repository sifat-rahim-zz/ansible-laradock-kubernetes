#!/usr/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION = '''
---
module: docker_ping
version_added: N/A
short_description: Try to connect to the docker daemon and return C(pong) on success.
description:
   - A test module to ensure that the docker daemon is functional.
options: {}
  unix_socket:
    description:
      - 'The unix docker socket to connect to'
    required: false
    default: '/var/run/docker.sock'
    aliases: []
author:
    - "Marvin Pinto"
'''

EXAMPLES = '''
- name: 'Ensure that the docker daemon is functional'
  docker_ping:

- name: 'Ensure that the docker daemon is functional'
  docker_ping: unix_socket="/var/run/docker.sock"
'''

import socket


def main():
    module = AnsibleModule(
        argument_spec = dict(
            unix_socket=dict(required=False, default='/var/run/docker.sock')
        ),
        supports_check_mode = False
    )

    params = module.params
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    failed_connection = False
    failed_msg = "pong"
    output = ""
    http_ok_string = "HTTP/1.0 200 OK"

    try:
        sock.connect(params['unix_socket'])
        sock.send("GET /info HTTP/1.0\r\n\r\n")
        buf = sock.recv(15)
        output = buf
    except socket.error as e:
        failed_connection = True
        failed_msg = str(e)
    finally:
        sock.close()

    if failed_connection:
        module.fail_json(msg=failed_msg)

    if not output == http_ok_string:
        module.fail_json(msg="Received '%s', expected '%s'" % (output, http_ok_string))

    module.exit_json(changed=False, ping="pong", raw=output)


from ansible.module_utils.basic import *
main()
