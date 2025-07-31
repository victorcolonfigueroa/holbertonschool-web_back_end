#!/usr/bin/env python3

#!/usr/bin/env python3
"""
Module that filters log messages
"""

import re
from typing import List, Tuple
import logging
import os
import mysql.connector


PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connects to a MySQL database
    """
    user = os.getenv("PERSONAL_DATA_DB_USERNAME")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD")
    host = os.getenv("PERSONAL_DATA_DB_HOST")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(user=user, password=password,
                                   host=host, database=db_name)


def get_logger() -> logging.Logger:
    """
    Returns a logging.Logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(handler)
    return logger


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Returns the log message obfuscated

    Args:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is
        separating all fields in the log line (message)

    The function should use a regex to replace occurrences
    of certain field values.

    filter_datum should be less than 5 lines long and
    use re.sub to perform the substitution with a single regex.

    Return:
        The log message obfuscated
    """
    for field in fields:
        message = re.sub(f'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}',
                         message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Filter values in incoming log records using filter_datum
        Values for fields in fields should be filtered
        """
        message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION,
                            message, self.SEPARATOR)


def main():
    """
    Main function:
        - Obtains a database connection using get_db
        - Retrieve all rows in the users table
        - Display each row under a filtered format
            - Filtered fields:
                - name
                - email
                - phone
                - ssn
                - password
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()
    logger.info("Retrieving users")
    for row in cursor:
        message = (f"name={row[0]}; email={row[1]}; phone={row[2]}; "
                   f"ssn={row[3]}; password={row[4]}; ip={row[5]}; "
                   f"last_login={row[6]}; user_agent={row[7]}")
        logger.info(message)
    cursor.close()
    db.close()


# Only the main function should run when the module is executed
if __name__ == "__main__":
    main()