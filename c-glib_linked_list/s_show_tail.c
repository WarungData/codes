#include <stdio.h>
#include <glib.h>

int main(void)
{
	GSList * slist = NULL;

	g_fprintf (stdout, "Jumlah node: %d\n", g_slist_length (slist));

	g_fprintf (stdout, "Tambahkan 'node 1' dan 'node 2'\n");
	slist = g_slist_append (slist, "node 1");
	slist = g_slist_append (slist, "node 2");
	
	g_fprintf (stdout, "Jumlah node: %d\n", g_slist_length (slist));

	g_fprintf (stdout, "\tTail: %s\n", g_slist_last (slist)-> data );

	g_slist_free (slist);

	return 0;

};

