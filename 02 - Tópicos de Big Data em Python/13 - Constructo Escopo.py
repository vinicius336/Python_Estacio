'''
    with open('./query.sql') as file:
        sql_query = file.read()
'''
try:
    file = open('./query.sql', 'r')
    sql_query = file.read()
exception Exception as e:
    print('Error:', e)
finally:
    file.close()