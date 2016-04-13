/*
 * (c) Nop, 2007, GPLv2.
 */

#include <stdio.h>
#include <libpq-fe.h>

#define MAX_LEN 255

int main(int argc, char * argv[])
{
	PGconn *conn;
	PGresult *res;
	char * query = calloc (MAX_LEN, sizeof (char));

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
		sprintf (query, "select version() as version");
		res = PQexec (conn, query);
		if (PQresultStatus (res) == PGRES_TUPLES_OK)
		{
			fprintf (stdout, "version: %s\n", PQgetvalue(res, 0,0));
		}
	}


	PQfinish (conn);

	return 0;
}
