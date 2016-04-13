#include <stdio.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include <errno.h>

int main ()
{
	int fd;
	char f_name[256];

	strcpy (f_name, "1.test");

	fd = open (f_name, O_WRONLY | O_CREAT);
	if (fd == -1)
	{
		fprintf (stderr, "%s\n", strerror(errno));
		exit (-1);
	}
	else
	{
		fprintf (stdout, "File %s created successfully with file descriptor %d\n", f_name, fd);
	}

	close (fd);
	return 0;

}
