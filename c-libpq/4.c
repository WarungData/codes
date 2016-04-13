/*
 * (c) Nop, 2007, GPLv2.
 */

#include <stdio.h>
#include <libpq-fe.h>

#define MAX_LEN 255
#define ROW_COUNT 100000

int main(int argc, char * argv[])
{
	PGconn *conn;
	PGresult *res;
	char * query = calloc (MAX_LEN, sizeof (char));
	int i;

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
		sprintf (query, "delete from b");
		res = PQexec (conn, query);
		if (PQresultStatus (res) == PGRES_COMMAND_OK)
		{
			fprintf (stdout, "done deleting content of b.\n");
			PQclear (res);
		}


		for (i=0; i< ROW_COUNT; i++)
		{	
			sprintf (query, "insert into b(b2) values ('row %d')", i);
			res = PQexec (conn, query);
			if (PQresultStatus (res) != PGRES_COMMAND_OK)
			{
				fprintf (stderr, "\tfailed on row: %d\n", i);
				exit (1);
			}
			PQclear (res);

			
		}
		fprintf (stdout, "done adding %d rows\n", ROW_COUNT);

	}


	PQfinish (conn);

	return 0;
}
