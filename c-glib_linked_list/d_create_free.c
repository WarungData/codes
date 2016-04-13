#include <stdio.h>
#include <glib.h>

int main(void)
{
	GList * dlist = NULL;

	g_fprintf (stdout, "Jumlah node: %d\n", g_list_length (dlist));

	g_list_free (dlist);

	return 0;

};

