#include <stdio.h>
#include <glib.h>

int main(void)
{
	GSList * slist = NULL, *curr = NULL;

	g_fprintf (stdout, "Jumlah node: %d\n", g_slist_length (slist));

	g_fprintf (stdout, "\tmenambahkan node: pertama\n");
	slist = g_slist_append (slist, "pertama");
	
	g_fprintf (stdout, "\tmenambahkan node: kedua\n");
	slist = g_slist_append (slist, "kedua");

	g_fprintf (stdout, "\tmenambahkan node: ketiga\n");
	slist = g_slist_append (slist, "ketiga");

	g_fprintf (stdout, "\tmenambahkan node: ketiga\n");
	slist = g_slist_append (slist, "ketiga");

	g_fprintf (stdout, "Jumlah node: %d\n", g_slist_length (slist));



	g_fprintf (stdout, "\tmenghapus semua node: ketiga\n");
	slist = g_slist_remove_all (slist, "ketiga");
	
	g_fprintf (stdout, "Jumlah node: %d\n", g_slist_length (slist));



	g_fprintf (stdout, "Iterasi: \n");

	for (curr = slist; curr; curr = curr -> next)
	{

		g_fprintf (stdout, "%s\n", curr -> data );
	}

	g_slist_free (slist);

	return 0;

};

