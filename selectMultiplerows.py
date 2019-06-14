import cx_Oracle

con = cx_Oracle.connect('system/manager@(DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = 100.73.21.146)(PORT = 1521)) (CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = nextdb) (INSTANCE_NAME = dmdb1)))')

print (con.version)

l_cursor = con.cursor()
l_execute = l_cursor.execute('SELECT PROGRAM, MODULE, MACHINE FROM V$SESSION')

print ( l_execute.rowcount )
print ( l_execute.fetchone() )

con.close()