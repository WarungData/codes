#include <gtk/gtk.h>

int main(int argc, char * argv[])
{
	GtkWidget *window, *label1, *label2, *label3, *table;

	gtk_init (&argc, &argv);

	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	gtk_widget_set_size_request (window, 400, 100);

	label1 = gtk_label_new ("Hello World :)");
	label2 = gtk_label_new ("): dlroW olleH");
	label3 = gtk_label_new ("World Hello :)");

	table = gtk_table_new (2, 2, TRUE);

	gtk_table_attach_defaults (GTK_TABLE (table), label1, 0, 1, 0, 1); 
	gtk_table_attach_defaults (GTK_TABLE (table), label2, 1, 2, 0, 1); 
	gtk_table_attach_defaults (GTK_TABLE (table), label3, 0, 1, 0, 2); 

	gtk_container_add (GTK_CONTAINER (window), table);

	gtk_widget_show_all (window);

	gtk_main();

	return 0;

};

