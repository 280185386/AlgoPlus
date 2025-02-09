# -*- coding: utf-8 -*-

import socket
from contextlib import closing


def check_service(ip, port):
    result = False
    try:
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            if sock.connect_ex((ip, port)) == 0:
                result = True  # OPEN
    except Exception as err_msg:
        print(f'check_service{err_msg}')
    finally:
        return result
