#include <stdio.h>
#include <glib.h>

int main(void)
{
	GSList * slist = NULL;

	g_fprintf (stdout, "Jumlah node: %d\n", g_slist_length (slist));

	g_slist_free (slist);

	return 0;

};

