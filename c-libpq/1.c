/*
 * (c) Nop, 2007, GPLv2.
 */

#include <stdio.h>
#include <libpq-fe.h>



int main(int argc, char * argv[])
{
	PGconn *conn;

	if (argc != 2)
	{
		fprintf (stderr, "usage: %s <connection_string>\n", argv[0]);
		return 1;
	}

	conn = PQconnectdb (argv[1]);

	if (PQstatus (conn) != CONNECTION_OK)
	{	

		fprintf (stderr, "Kesalahan koneksi: %s\n", PQerrorMessage (conn));
	}
	else
	{
		fprintf (stdout, "connected:\n");
		fprintf (stdout, "\tto host: %s\n", PQhost (conn));
		fprintf (stdout, "\tto database: %s\n", PQdb (conn));
		fprintf (stdout, "\tas user: %s\n", PQuser (conn));

	}


	fprintf (stdout, "disconnecting...");
	PQfinish (conn);
	fprintf (stdout, "done\n");

	return 0;
}
