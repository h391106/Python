import cx_Oracle

con = cx_Oracle.connect('system/manager@(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = 100.73.21.146)(PORT = 1521)) (CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = nextdb) (INSTANCE_NAME = dmdb1)))')

print (con.version)

l_cursor = con.cursor()
l_cursor.execute('SELECT HOST_NAME, INSTANCE_NAME FROM V$INSTANCE')

for row in l_cursor:
 print (row)

con.close()