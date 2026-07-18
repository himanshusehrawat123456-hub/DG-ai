"""
DG AI Version 1
Search Index

Purpose:
- Create searchable index
- Store indexed data
- Provide fast lookup foundation

Version: 1.0
"""

import logging
from datetime import datetime


class SearchIndex:
    """
    Professional Search Index Manager
    """

    def __init__(self):

        self.index = {}

        self.history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def tokenize(
        self,
        text
    ):
        """
        Convert text into keywords.
        """

        if not isinstance(
            text,
            str
        ):

            return []


        words = text.lower().split()


        return words


    # ---------------------------------

    def add_document(
        self,
        document_id,
        content
    ):
        """
        Add document to index.
        """

        keywords = self.tokenize(
            content
        )


        for word in keywords:

            if word not in self.index:

                self.index[word] = []


            if document_id not in self.index[word]:

                self.index[word].append(
                    document_id
                )


        self.history.append({

            "action": "add",

            "document":
            document_id,

            "time":
            str(datetime.now())

        })


        return True


    # ---------------------------------

    def remove_document(
        self,
        document_id
    ):
        """
        Remove document from index.
        """

        for word in self.index:

            if document_id in self.index[word]:

                self.index[word].remove(
                    document_id
                )


        return True


    # ---------------------------------

    def search_keyword(
        self,
        keyword
    ):
        """
        Search document IDs.
        """

        keyword = keyword.lower()


        return self.index.get(
            keyword,
            []
        )


    # ---------------------------------

    def get_index(self):
        """
        Return complete index.
        """

        return self.index


    # ---------------------------------

    def clear_index(self):
        """
        Clear all index data.
        """

        self.index.clear()

        return True


    # ---------------------------------

    def get_history(self):

        return self.history



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    search = SearchIndex()


    search.add_document(
        1,
        "DG AI artificial intelligence project"
    )


    print(
        search.search_keyword(
            "ai"
        )
    )
