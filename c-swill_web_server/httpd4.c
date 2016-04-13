/*
 * (c) Nop
 * GPL
 */


#include <stdio.h>
#include <swill/swill.h>
#include <time.h>

#define PORT 9001

void do_hello (FILE *f)
{
	fprintf (f, "Hello World.\n");
}

void do_info (FILE *f)
{
	fprintf (f, "Info: Sky is blue.\n");
}

int main(void)
{
	if (!swill_init (PORT))
	{
		fprintf (stderr, "Error occured.\n");
		return 1;
	}

	swill_file ("index.html", 0);
	swill_handle ("hello", do_hello, 0);
	swill_handle ("info", do_info, 0);

	swill_log (stdout);
	
	fprintf (stdout, "Server started on port %d.\n", PORT);


	while (1)
	{
		swill_serve ();
	}

	return 0;
}

