/*
 * (c) Nop
 * GPL
 */


#include <stdio.h>
#include <swill/swill.h>

#define PORT 9001


int main(void)
{
	if (!swill_init (PORT))
	{
		fprintf (stderr, "Error occured.\n");
		return 1;
	}

	fprintf (stdout, "Server started on port %d.\n", PORT);

	while (1)
	{
		swill_serve ();
	}

	return 0;
}

