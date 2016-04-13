/*
 * (c) Nop
 * GPL
 */


#include <stdio.h>
#include <swill/swill.h>
#include <math.h>

#define PORT 9001


void do_sqrt (FILE *f)
{
	double x;
	if (!swill_getargs ("d(x)", &x))
	{
		fprintf (f, "Error. Please supply x.\n");
	}
	else
	{
		fprintf (f, "Square root of %f is %f.\n", x, sqrt (x));
	}
}

void do_strx (FILE *f)
{
	int x;
	char *s;
	int i = 0;

	if (!swill_getargs ("i(x)s(s)", &x, &s))
	{
		fprintf (f, "Error. Please supply x and s.\n");
	}
	else
	{
		for  (i=0; i<x; i++)
		{
			fprintf (f, "%s", s);
		}
	}
}

void do_sayhello (FILE *f)
{
	char *name;
	char *os = NULL;

	if (!swill_getargs ("s(name)|s(os)", &name, &os))
	{
		fprintf (f, "Error. Please supply name and os (optional).\n");
	}
	else
	{
		fprintf (f, "Hello, %s. Where do you want to go today?\n", name);

		if (os != NULL)
		{
			if (strcasecmp(os, "linux") == 0)
			{
				fprintf (f, "You are using Linux. You are going somewhere fun :)");
			}
			else
			{
				fprintf (f, "You are using %s", os);
			}	

		}

	}
}

int main(void)
{
	if (!swill_init (PORT))
	{
		fprintf (stderr, "Error occured.\n");
		return 1;
	}

	swill_handle ("sqrt", do_sqrt, 0);
	swill_handle ("strx", do_strx, 0);
	swill_handle ("sayhello", do_sayhello, 0);

	fprintf (stdout, "Server started on port %d.\n", PORT);

	while (1)
	{
		swill_serve ();
	}

	return 0;
}

