import init_database


def task_1_add_new_record_to_db(con) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """

    cur = con.cursor()
    cur.execute("""INSERT INTO Customers(CustomerName,ContactName,Address,City,PostalCode,Country) 
                                 VALUES('Thomas', 'David', 'Some Address', 'London', '774', 'Singapore')""")
    con.commit()
    return cur.fetchall()


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    sql = '''SELECT * FROM Customers'''
    cur.execute(sql)
    return cur.fetchall()


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    sql = """
    SELECT * FROM Customers WHERE Country LIKE 'G%ny'
    """
    cur.execute(sql)
    return cur.fetchall()


def task_4_update_customer(con):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        con: psycopg cursor

    Returns: 91 records with updated customer

    """
    sql = '''UPDATE Customers
             SET CustomerName = 'Johnny Depp'
                   WHERE CustomerID = (
                                       SELECT min(CustomerID) from Customers
                                      )
          '''
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    return cur.fetchall()

    
def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """
    sql = ''' DELETE FROM Customers 
                         WHERE CustomerID = (
                                             SELECT max(CustomerID) from Customers
                                             ) '''
    cur = con.cursor()
    cur.execute(sql)
    con.commit()


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    sql = ''' SELECT DISTINCT Country FROM Suppliers
              ORDER BY Country'''
    cur.execute(sql)
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    sql = ''' SELECT DISTINCT Country FROM Suppliers
              ORDER BY Country DESC'''
    cur.execute(sql)
    return cur.fetchall()


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    sql = '''SELECT City, count(CustomerID) count_id FROM Customers 
             GROUP BY City 
             ORDER BY City'''

    cur.execute(sql)
    return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    sql = '''SELECT Country, count(CustomerID) CountOfCustomers FROM Customers
             GROUP BY Country
             HAVING count(CustomerID) > 10 '''
    cur.execute(sql)
    return cur.fetchall()


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers from the table

    Results: 10 records
    """
    sql = '''SELECT * FROM Customers 
                                    WHERE ROWNUM < 11'''
    cur.execute(sql)
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    sql = '''SELECT * FROM Customers
                                    WHERE CustomerID >= 11 '''
    cur.execute(sql)
    return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    sql = '''SELECT * FROM Suppliers 
                                    WHERE Country in('USA','UK','Japan');'''
    cur.execute(sql)
    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    sql = '''SELECT * FROM Products p JOIN Suppliers s 
                                        ON p.SupplierID = s.SupplierID
                    WHERE Country LIKE "Sw%n"'''
    cur.execute(sql)
    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    sql = '''SELECT * FROM Products p LEFT JOIN Supplier s 
                                             ON p.SupplierID=s.SupplierID'''
    cur.execute(sql)
    return cur.fetchall()


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    sql = '''SELECT * FROM Customers c LEFT JOIN Orders o 
                                              ON c.CustomerID = o.CustomerID'''
    cur.execute(sql)
    return cur.fetchall()


def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    sql = '''SELECT * FROM Customers c FULL JOIN Suppliers s 
                                              ON c.Country = s.Country '''
    cur.execute(sql)
    return cur.fetchall()



