#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

int main (int argc, char * argv[])
{
	int fd;
	int res;
	
	struct stat stat_buf;

	if (argc != 2)
	{
		fprintf (stderr, "usage %s <file>\n", argv[0]);
		exit (1);
	}

	fd = open (argv[1], O_RDONLY);

	res = fstat (fd, &stat_buf);
	
	if (res == 0)
	{
		fprintf (stdout, "Size of %s is %ld byte\n", argv[1], stat_buf.st_size);
	}
	else
	{
		fprintf (stderr, "%s\n", strerror(errno));
		exit (-1);
	}

	close (fd);

	return 0;

}
