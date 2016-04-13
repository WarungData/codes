/*
 * (c) Nop
 * GPL
 */


#include <stdio.h>
#include <swill/swill.h>
#include <time.h>

#define PORT 9001
#define DOCROOT "/tmp/web/"
#define CGIROOT "/tmp/cgi/"

void do_list ()
{
	char cmd[255];
	sprintf (cmd, "ls -al %s", DOCROOT);
	system (cmd); 
}

void do_listhtml ()
{
	char cmd[255];
	sprintf (cmd, "%s/list.cgi %s", CGIROOT, DOCROOT);
	system (cmd); 
}

void do_fortune ()
{
	system ("fortune"); 
}

int main(void)
{
	if (!swill_init (PORT))
	{
		fprintf (stderr, "Error occured.\n");
		return 1;
	}

	swill_file ("index.html", 0);
	swill_handle ("stdout:list", do_list, 0);
	swill_handle ("stdout:list.html", do_listhtml, 0);
	swill_handle ("stdout:fortune", do_fortune, 0);

	swill_directory (DOCROOT);

	swill_log (stdout);
	
	fprintf (stdout, "Server started on port %d (docroot: %s).\n", PORT, DOCROOT);

	while (1)
	{
		swill_serve ();
	}

	return 0;
}

