"""
DG AI Version 1
Document Manager

Purpose:
- Manage documents
- Track document information
- Control document operations

Version: 1.0
"""

import logging
from datetime import datetime


class DocumentManager:
    """
    Professional Document Management System
    """

    def __init__(self):

        self.documents = []

        self.history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def create_document(
        self,
        name,
        document_type="text"
    ):
        """
        Create document record.
        """

        document = {

            "id": len(self.documents) + 1,

            "name": name,

            "type": document_type,

            "status": "created",

            "created_at": str(datetime.now())

        }


        self.documents.append(
            document
        )


        self.log_action(
            "Document Created",
            document
        )


        return document


    # ---------------------------------

    def get_document(
        self,
        document_id
    ):
        """
        Find document by ID.
        """

        for document in self.documents:

            if document["id"] == document_id:

                return document


        return None


    # ---------------------------------

    def update_status(
        self,
        document_id,
        status
    ):
        """
        Update document status.
        """

        document = self.get_document(
            document_id
        )


        if document:

            document["status"] = status

            self.log_action(
                "Status Updated",
                document
            )

            return True


        return False


    # ---------------------------------

    def delete_document(
        self,
        document_id
    ):
        """
        Delete document record.
        """

        document = self.get_document(
            document_id
        )


        if document:

            self.documents.remove(
                document
            )

            self.log_action(
                "Document Deleted",
                document
            )

            return True


        return False


    # ---------------------------------

    def get_all_documents(self):

        return self.documents


    # ---------------------------------

    def log_action(
        self,
        action,
        data
    ):

        self.history.append({

            "action": action,

            "data": data,

            "time": str(datetime.now())

        })


    # ---------------------------------

    def get_history(self):

        return self.history



# Testing

if __name__ == "__main__":

    manager = DocumentManager()

    print(
        manager.create_document(
            "DG_AI_Report.pdf",
            "pdf"
        )
    )
