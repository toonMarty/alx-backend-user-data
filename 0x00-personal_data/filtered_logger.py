#!/usr/bin/env python3
"""
This module contains:
    a tuple PII_FIELDS which is constant at the root and
    contains fields from user_data.csv considered as PII
    A format method to filter values in incoming log records
    A Redacting Formatter class, RedactingFormatter
    A get logger function that returns a logging.getLogger object
"""
from typing import List
import re
import os
import mysql.connector
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        This method initializes instances of RedactingFormatter
        Args:
            fields(List[str]): a list of string fields
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        This method filters values in incoming log records using
        filter_datum
        Args:
            record(logging.LogRecord): a logging record instance
        Return:
            filtered_values(str): a string of values for filtered fields
        """
        filtered_values = filter_datum(self.fields, self.REDACTION,
                                       super().format(record), self.SEPARATOR)
        return filtered_values


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    This function obfuscates a log message
    Args:
        fields(List): a list of strings representing all fields to obfuscate
        redaction (str): a string representing what field will be obfuscated
        message(str): a string representing the log line
        separator(str): a string representing by which character
        is separating all the fields in the log line(message)
    Return:
        Obfuscated log message
    """
    for item in fields:
        message = re.sub(fr'{item}=.+?{separator}',
                         f'{item}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """
    This function contains a logger named user_data
    It logs uo to logging.INFO level
    It does not propagate messages to other loggers
    It has a StreamHandler with RedactingFormatter as formatter
    Return:
        logging.Logger object
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    This function returns a connector to the database
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD")
    host = os.getenv("PERSONAL_DATA_DB_HOST")
    database = os.getenv("PERSONAL_DATA_DB_NAME")
    return mysql.connector.connect(user=username,
                                   password=password,
                                   host=host,
                                   database=database
                                   )


def main():
    """
    The function obtains a database connection
    using get_db and retrieves all rows in the users
    table and displays each row under a filtered format
    """
    connection = get_db()
    users = connection.cursor()
    users.execute(
        "SELECT CONCAT('name=', name, "
        "';ssn=', ssn, "
        "';ip=', ip, "
        "';user_agent', user_agent, ';') AS message FROM users;")
    RedactingFormatter(fields=PII_FIELDS)
    logger = get_logger()

    for user in users:
        logger.log(logging.INFO, user[0])


if __name__ == "__main__":
    main()
