#include <stdio.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include <errno.h>

int main ()
{
	int fd1, fd2, fd3;

	fd1 = open ("1b.test.1", O_WRONLY | O_CREAT, S_IRWXU );
	fd2 = open ("1b.test.2", O_WRONLY | O_CREAT, S_IRUSR | S_IWUSR | S_IRGRP );
	fd2 = open ("1b.test.3", O_WRONLY | O_CREAT, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH);

	close (fd1);
	close (fd2);
	close (fd3);

	return 0;

}
