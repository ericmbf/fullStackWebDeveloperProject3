#!/usr/bin/env python3
import psycopg2

OUTPUT1 = '''\
    "%s" - %s views
'''

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

    # Ger cursor
    cursor = conn.cursor()
    
    #Build query
    cursor.execute("""select title, count(*) as views
                        from articles, log
                        where path like CONCAT('%', slug)
                        group by title
                        order by views desc
                        limit {};""".format(limit))
    
    # Get result
    result = cursor.fetchall()

    # Close database
    conn.close()

    return result

def databaseConnect():
    return psycopg2.connect("dbname=news")
  
if __name__== "__main__":
    limit = 3
    print("The most {} popular articles are:".format(limit))
    result = "".join(OUTPUT1 % (title, view) for title, view in getMostPopular(limit))
    print(result)