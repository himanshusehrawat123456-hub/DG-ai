"""
DG AI Version 1
Security Audit System

Purpose:
- Record security audit events
- Maintain audit history

Version: 1.0
"""

import datetime


class SecurityAudit:
    """
    Handles security audit operations.
    """

    def __init__(self):
        self.audit_logs = []

    def add_audit(self, module, action, status):
        """
        Add a security audit record.
        """

        record = {
            "id": len(self.audit_logs) + 1,
            "module": module,
            "action": action,
            "status": status,
            "time": str(datetime.datetime.now())
        }

        self.audit_logs.append(record)

        return record

    def get_audit_logs(self):
        """
        Return all audit records.
        """

        return self.audit_logs

    def clear_audit_logs(self):
        """
        Clear all audit records.
        """

        self.audit_logs.clear()

        return True


# Testing

if __name__ == "__main__":

    audit = SecurityAudit()

    print(
        audit.add_audit(
            "Login System",
            "User Login",
            "Success"
        )
    )

    print(
        audit.get_audit_logs()
    )
