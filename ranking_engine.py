"""
DG AI Version 1
Ranking Engine System

Purpose:
- Rank responses
- Select best result

Version: 1.0
"""


import datetime



class RankingEngine:
    """
    Handles DG AI ranking operations.
    """



    def __init__(self):

        self.rank_history = []



    def calculate_score(self, response):
        """
        Calculate basic response score.
        """

        score = len(
            response
        )


        return score



    def rank_responses(self, responses):
        """
        Rank multiple responses.
        """

        ranked = sorted(
            responses,
            key=self.calculate_score,
            reverse=True
        )


        record = {

            "responses":
            responses,

            "ranked":
            ranked,

            "time":
            str(datetime.datetime.now())

        }


        self.rank_history.append(record)


        return ranked



    def get_history(self):
        """
        Return ranking history.
        """

        return self.rank_history



    def clear_history(self):
        """
        Clear ranking history.
        """

        self.rank_history.clear()

        return True




# Testing

if __name__ == "__main__":


    engine = RankingEngine()


    responses = [

        "Hi",

        "Hello, how can I help you today?"

    ]


    print(
        engine.rank_responses(
            responses
        )
    )
