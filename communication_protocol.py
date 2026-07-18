"""
DG AI Version 1
Communication Protocol System

Purpose:
- Define communication rules
- Manage message protocols

Version: 1.0
"""


import datetime



class CommunicationProtocol:
    """
    Handles communication protocols.
    """



    def __init__(self):

        self.protocols = []



    def create_protocol(self, name, protocol_type):
        """
        Create communication protocol.
        """

        protocol = {

            "id":
            len(self.protocols) + 1,

            "name":
            name,

            "type":
            protocol_type,

            "status":
            "Active",

            "time":
            str(datetime.datetime.now())

        }


        self.protocols.append(protocol)


        return protocol



    def disable_protocol(self, name):
        """
        Disable protocol.
        """

        for protocol in self.protocols:

            if protocol["name"] == name:

                protocol["status"] = "Disabled"

                return True


        return False



    def get_protocols(self):
        """
        Return all protocols.
        """

        return self.protocols




# Testing

if __name__ == "__main__":


    cp = CommunicationProtocol()


    cp.create_protocol(
        "Chat Protocol",
        "Internal"
    )


    print(
        cp.get_protocols()
    )
