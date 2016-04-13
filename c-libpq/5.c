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
	char * conninfo = calloc (MAX_LEN, sizeof (char));
	char * query = calloc (MAX_LEN, sizeof (char));
	char * nama = calloc (MAX_LEN, sizeof (char));
	char * alamat = calloc (MAX_LEN, sizeof (char));
	char * temp = calloc (MAX_LEN, sizeof (char));
	int field_count;
	int rec_count;
	int c,menu;
	int i,j;

	strcpy (conninfo, "dbname=test user=nop");
	conn = PQconnectdb (conninfo);

	if (PQstatus (conn) != CONNECTION_OK)
	{	

		fprintf (stderr, "Kesalahan koneksi: %s\n", PQerrorMessage (conn));
		exit (1);
	}

	while ( 1 )
	{
		fprintf(stdout, "\n\n\nDATA PASIEN\n");
		fprintf(stdout, "***********\n\n");
		fprintf(stdout, "a Tambah data\n");
		fprintf(stdout, "b Tampil data\n");
		fprintf(stdout, "x Keluar aplikasi\n");
		fprintf(stdout, "Pilihan Anda: ");
		c = tolower(fgetc (stdin));
		menu = c;

		while (c != '\n' && c != EOF) c = fgetc (stdin);

		if (menu == 'a')
		{
			fprintf(stdout, "Tambah data\n");
			fprintf(stdout, "===========\n");
			fprintf(stdout, "Nama    : ");
			fgets (nama, MAX_LEN-1, stdin);
			fprintf(stdout, "Alamat  : ");
			fgets (alamat, MAX_LEN-1, stdin);
			sprintf (query, "insert into pasien (nama, alamat) values ('%s','%s')", nama, alamat);
			res = PQexec (conn, query);
			PQclear (res);
		}
		else
		if (menu == 'b')
		{
			fprintf(stdout, "Tampil data\n");
			fprintf(stdout, "===========\n");
			sprintf (query, "select nama,alamat from pasien");
			res = PQexec (conn, query);
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
					strcpy (temp, PQgetvalue (res, i, j));
					temp[strlen(temp)-1] = 0;
					fprintf (stdout, "%-40s", temp);
				}
				fprintf (stdout, "\n");
			}

			PQclear (res);


		}
		else
		if (menu == 'x')
		{
			fprintf(stdout, "Bye\n");
			break;

		}
	};
	
	PQfinish (conn);

	free (nama);
	free (alamat);
	free (query);
	free (conninfo);
	free (temp);

	return 0;
}
