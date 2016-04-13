/*
 * (c) Nop
 * GPL
 */


#include <stdio.h>
#include <swill/swill.h>

#define PORT 9001

int mp = 0;
static int n = 0;

void do_mode (FILE *f)
{
	int m;
	if (!swill_getargs("i(m)", &m))
	{
		fprintf (f, "Error. Please supply m=0 or m=1.");
	}
	else
	{
		if (m == 0)
		{
			fprintf (f, "OK. Set m=0");
			mp = 0;
		}
		else
		if (m == 1)
		{
			fprintf (f, "OK. Set m=1");
			mp = 1;
		}
		else
		{
			fprintf (f, "Error. Don't know what to do. ");
		}
	}
}

void print_number()
{

	n++;
	if (n > 99999) n = 0;

	if (mp == 0)
	{
		if (n % 2 == 0)
		{	
			fprintf (stdout, "\r[even]%d      ", n);
		}
	}
	else
	if (mp == 1)
	{
		if (n % 2 == 1)
		{	
			fprintf (stdout, "\r[odd ]%d      ", n);
		}
	}
}

int main(void)
{
	int c=0;

	if (!swill_init (PORT))
	{
		fprintf (stderr, "Error occured.\n");
		return 1;
	}


	fprintf (stdout, "Server started on port %d.\n", PORT);

	swill_handle ("mode", do_mode, 0);

	while (1)
	{
		/*
		 * multitasking counter
		 *
		 */
		c++;
		if (c > 10000) c = 0;



		/*
		 * simple multitasking :)
		 * print number on lower priority
		 */
		if (c % 9 == 0)
		{
			print_number();
		}
		else
		{
			swill_poll();
		}
	}

	return 0;
}

