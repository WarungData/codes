#include <stdio.h>
#include <glib.h>

gint comp_strcasecmp (gconstpointer item1, gconstpointer item2)
{
	return g_ascii_strcasecmp (item1, item2);
}

int main(void)
{
	GSList * slist = NULL, *curr = NULL;

	g_fprintf (stdout, "Jumlah node: %d\n", g_slist_length (slist));

	g_fprintf (stdout, "\tmenambahkan node: satu\n");
	slist = g_slist_append (slist, "satu");
	
	g_fprintf (stdout, "\tmenambahkan node: dua\n");
	slist = g_slist_append (slist, "dua");

	g_fprintf (stdout, "\tmenambahkan node: tiga\n");
	slist = g_slist_append (slist, "tiga");

	g_fprintf (stdout, "Jumlah node: %d\n", g_slist_length (slist));
	

	g_fprintf (stdout, "Iterasi (tanpa sort): \n");

	for (curr = slist; curr; curr = curr -> next)
	{

		g_fprintf (stdout, "%s\n", curr -> data );
	}


	slist = g_slist_sort (slist, (GCompareFunc) comp_strcasecmp);

	g_fprintf (stdout, "Iterasi (dengan sort): \n");

	for (curr = slist; curr; curr = curr -> next)
	{

		g_fprintf (stdout, "%s\n", curr -> data );
	}

	g_slist_free (slist);

	return 0;

};

