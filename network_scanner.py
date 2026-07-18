"""
DG AI Version 1
Network Scanner
"""

import socket


class NetworkScanner:

    def scan_host(self, host):

        try:

            ip = socket.gethostbyname(host)

            return {
                "host": host,
                "ip": ip,
                "status": "Reachable"
            }

        except socket.gaierror:

            return {
                "host": host,
                "ip": None,
                "status": "Not Found"
            }


if __name__ == "__main__":

    scanner = NetworkScanner()

    print(
        scanner.scan_host("google.com")
    )
