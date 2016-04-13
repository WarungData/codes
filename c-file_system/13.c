#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <sys/types.h>
#include <dirent.h>

int main (int argc, char * argv[])
{

	DIR *d;
	
	struct dirent * direntry;

	if (argc != 2)
	{
		fprintf (stderr, "usage %s <dir>\n", argv[0]);
		exit (1);
	}

	d = opendir (argv[1]);

	if (d == NULL)
	{
		fprintf (stderr, "%s\n", strerror (errno));
		exit (2);
	}

	direntry = readdir (d);

	while (direntry  != NULL)
	{

		fprintf (stdout, "%s\n", direntry -> d_name);
		direntry = readdir (d);
	}

	closedir(d);

	return 0;

}
