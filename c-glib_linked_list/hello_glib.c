#include <stdio.h>
#include <glib.h>

int main(void)
{
	GString *gstr = g_string_new ("Hello from GLib");
	
	g_fprintf (stdout, "\n%s\n", gstr -> str);
	
	g_string_free (gstr, TRUE);

	return 0;
};

