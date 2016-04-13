#include <stdio.h>
#include <unistd.h>
#include <errno.h>

int main (int argc, char * argv[])
{

	char ref_file[256];
	int len;

	if (argc != 2)
	{
		fprintf (stderr, "usage %s <file>\n", argv[0]);
		exit (1);
	}

	len = readlink (argv[1], ref_file, sizeof (ref_file));

	if (len == -1)
	{
		fprintf (stderr, "%s\n", strerror(errno));
		exit (-1);
	}
	else
	{
		ref_file[len] = '\0';
		fprintf (stdout, "%s is symlink to %s\n", argv[1], ref_file);
	}

	return 0;

}
