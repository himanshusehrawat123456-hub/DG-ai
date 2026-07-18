"""
DG AI Version 1
Agent Management System

Purpose:
- Manage AI agents
- Register and control agents
- Provide multi-agent foundation

Version: 1.0
"""


import datetime



class AgentManager:
    """
    Handles DG AI agent operations.
    """



    def __init__(self):

        self.agents = []



    def create_agent(self, name, role):
        """
        Create a new AI agent.

        Parameters:
            name: Agent name
            role: Agent purpose
        """

        agent = {

            "id":
            len(self.agents) + 1,

            "name":
            name,

            "role":
            role,

            "status":
            "Active",

            "created":
            str(datetime.datetime.now())

        }


        self.agents.append(agent)


        return agent



    def get_agents(self):
        """
        Return all agents.
        """

        return self.agents



    def find_agent(self, name):
        """
        Search agent by name.
        """

        for agent in self.agents:

            if agent["name"] == name:

                return agent


        return None



    def deactivate_agent(self, agent_id):
        """
        Disable an agent.
        """

        for agent in self.agents:

            if agent["id"] == agent_id:

                agent["status"] = "Inactive"

                return True


        return False




# Testing

if __name__ == "__main__":


    manager = AgentManager()


    manager.create_agent(
        "Assistant Agent",
        "General Help"
    )


    manager.create_agent(
        "Research Agent",
        "Information Research"
    )


    print(
        "DG AI Agents:"
    )


    print(
        manager.get_agents()
    )
