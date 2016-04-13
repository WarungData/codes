#include <stdio.h>
#include "matematika.h"

int main(void)
{
	fprintf (stdout, "25 kuadrat = %f\n", kuadrat(25));
	fprintf (stdout, "Bilangan terbesar antara 10 dan 20 adalah  %f\n", lebihbesar(10,20));
	fprintf (stdout, "Bilangan terkecil antara 10 dan 20 adalah  %f\n", lebihkecil(10,20));

	return 0;
}
