#!/usr/bin/env python3
import psycopg2


def getMostPopular(limit):
    """
        Return the most popular articles from table news.
    Args:
        limit (int): The number of records.
    Returns:
        string: The result query from the most popular articles limited by 
        limit argument.
    """
    # Connect database
    conn = databaseConnect()

    #Build query

    #Exec query

    # Close database
    conn.close()


def databaseConnect():
    return psycopg2.connect("dbname=news")
  
if __name__== "__main__":
    limit = 5
    print("The most {} popular articles:\n".format(limit))
    print(getMostPopular(limit))