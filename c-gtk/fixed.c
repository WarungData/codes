#include <gtk/gtk.h>

int main(int argc, char * argv[])
{
	GtkWidget *window, *label1, *label2, *label3, *fixed;

	gtk_init (&argc, &argv);

	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	gtk_widget_set_size_request (window, 400, 100);

	label1 = gtk_label_new ("Hello World :)");
	label2 = gtk_label_new ("): dlroW olleH");
	label3 = gtk_label_new ("World Hello :)");

	fixed = gtk_fixed_new ();

	gtk_fixed_put (GTK_FIXED (fixed), label1, 10, 10);
	gtk_fixed_put (GTK_FIXED (fixed), label2, 300, 50);
	gtk_fixed_put (GTK_FIXED (fixed), label3, 100, 10);

	gtk_container_add (GTK_CONTAINER (window), fixed);

	gtk_widget_show_all (window);

	gtk_main();

	return 0;

};

