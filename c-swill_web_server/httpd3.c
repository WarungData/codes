/*
 * (c) Nop
 * GPL
 */


#include <stdio.h>
#include <swill/swill.h>

#define PORT 9001
#define DOCROOT "/tmp/web/"

int main(void)
{
	if (!swill_init (PORT))
	{
		fprintf (stderr, "Error occured.\n");
		return 1;
	}

	swill_directory (DOCROOT);

	fprintf (stdout, "Server started on port %d (docroot: %s).\n", PORT, DOCROOT);

	while (1)
	{
		swill_serve ();
	}

	return 0;
}

