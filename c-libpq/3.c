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
	int field_count;
	int rec_count;
	int i,j;

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
		sprintf (query, "select nama,alamat from a");
		res = PQexec (conn, query);
		if (PQresultStatus (res) == PGRES_TUPLES_OK)
		{
			field_count = PQnfields (res);
			for (i=0; i< field_count; i++)
			{
				fprintf (stdout, "%-40s", PQfname (res, i));
			}
			fprintf (stdout, "\n");

			rec_count = PQntuples (res);
			for (i=0; i< rec_count; i++)
			{
				for (j=0; j< field_count; j++)
				{
					fprintf (stdout, "%-40s", PQgetvalue (res, i, j));
				}
				fprintf (stdout, "\n");
			}

			PQclear (res);

		}
	}


	PQfinish (conn);

	return 0;
}
