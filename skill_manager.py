"""
DG AI Version 1
Skill Manager System

Purpose:
- Manage skills
- Track skill progress

Version: 1.0
"""


import datetime



class SkillManager:
    """
    Handles skill management operations.
    """



    def __init__(self):

        self.skills = []



    def add_skill(self, name, level="Beginner"):
        """
        Add new skill.
        """

        skill = {

            "id":
            len(self.skills) + 1,

            "name":
            name,

            "level":
            level,

            "status":
            "Learning",

            "time":
            str(datetime.datetime.now())

        }


        self.skills.append(skill)


        return True



    def update_skill(self, name, level, status):
        """
        Update skill progress.
        """

        for skill in self.skills:

            if skill["name"] == name:

                skill["level"] = level

                skill["status"] = status

                return True


        return False



    def get_skills(self):
        """
        Return all skills.
        """

        return self.skills



    def remove_skill(self, name):
        """
        Remove skill.
        """

        for skill in self.skills:

            if skill["name"] == name:

                self.skills.remove(skill)

                return True


        return False




# Testing

if __name__ == "__main__":


    manager = SkillManager()


    manager.add_skill(
        "Python",
        "Intermediate"
    )


    manager.update_skill(
        "Python",
        "Advanced",
        "Completed"
    )


    print(
        manager.get_skills()
    )
