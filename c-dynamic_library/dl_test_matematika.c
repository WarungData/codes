#include <stdio.h>
#include <dlfcn.h>

int main(void)
{
	void *handle_matematika;

	double (*kuadrat) (double);
	double (*lebihbesar) (double,double);
	double (*lebihkecil) (double,double);

	handle_matematika = dlopen("./libmatematika.so", RTLD_LAZY);

	kuadrat = dlsym(handle_matematika, "kuadrat");
	lebihbesar = dlsym(handle_matematika, "lebihbesar");
	lebihkecil = dlsym(handle_matematika, "lebihkecil");


	fprintf (stdout, "25 kuadrat = %f\n", (*kuadrat)(25));
	fprintf (stdout, "Bilangan terbesar antara 10 dan 20 adalah  %f\n", (*lebihbesar) (10,20));
	fprintf (stdout, "Bilangan terkecil antara 10 dan 20 adalah  %f\n", (*lebihkecil) (10,20));


	dlclose (handle_matematika);

	return 0;
}
