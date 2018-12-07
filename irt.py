#!/usr/bin/env python3
import psycopg2

OUTPUT1 = '''\
    "%s" - %s views'''

OUTPUT2 = '''\
    "%s" - %s errors'''
    
def databaseConnect():
    return psycopg2.connect("dbname=news")

def getMostPopularArticles(limit):
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

def getMostPopularAuthors():
    """
        Return the most popular author from table news.
    Args:
    Returns:
        string: The result query from the most popular author.
    """
    # Connect database
    conn = databaseConnect()

    # Ger cursor
    cursor = conn.cursor()

    #Build query
    cursor.execute("""select name, count(*) as views
                        from articles, log, authors
                        where path like CONCAT('%', slug)
                        and articles.author = authors.id
                        group by authors.name
                        order by views desc;""")

    # Get result
    result = cursor.fetchall()

    # Close database
    conn.close()

    return result

def getDaysWithErrorPerCent(percent):
    """
        Return the most popular author from table news.
    Args:
        percent (float): the percent number limit.
    Returns:
        string: The result query with days and error per cent from above limit
        percent. 
        
    """
    # Connect database
    conn = databaseConnect()

    # Ger cursor
    cursor = conn.cursor()

    #Build query
    cursor.execute("""select get_all.date as date, 
                    ((get_error.req * 100.0) / get_all.req) as error
                    from get_all, get_error 
                    where get_all.date = get_error.date and
                    get_error.req > (get_all.req * {0:.2f});""".format(float(percent)/100))

    # Get result
    result = cursor.fetchall()

    # Close database
    conn.close()

    return result

if __name__== "__main__":
    limit = 3
    print("The most {} popular articles are:".format(limit))
    result = "".join(OUTPUT1 % (title, view) for title, view in getMostPopularArticles(limit))
    print(result)

    print("The most popular authors are:")
    result = "".join(OUTPUT1 % (name, view) for name, view in getMostPopularAuthors())
    print(result)

    percent = 1
    print("The Days that {}% of requests are errors:".format(percent))
    result = "".join(OUTPUT2 % (date, error) for date, error in getDaysWithErrorPerCent(percent))
    print(result)
