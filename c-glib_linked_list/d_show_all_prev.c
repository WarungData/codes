#include <stdio.h>
#include <glib.h>

int main(void)
{
	GList * dlist = NULL, *curr = NULL;

	g_fprintf (stdout, "Jumlah node: %d\n", g_list_length (dlist));

	g_fprintf (stdout, "\tmenambahkan node: pertama\n");
	dlist = g_list_append (dlist, "pertama");
	
	g_fprintf (stdout, "\tmenambahkan node: kedua\n");
	dlist = g_list_append (dlist, "kedua");

	g_fprintf (stdout, "\tmenambahkan node: ketiga\n");
	dlist = g_list_append (dlist, "ketiga");

	g_fprintf (stdout, "Jumlah node: %d\n", g_list_length (dlist));
	

	g_fprintf (stdout, "Iterasi (prev): \n");

	for (curr = g_list_last(dlist)  ; curr; curr = curr -> prev)
	{

		g_fprintf (stdout, "%s\n", curr -> data );
	}

	g_list_free (dlist);

	return 0;

};

