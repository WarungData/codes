#include <gtk/gtk.h>

int main (int argc, char *argv[])
{
	GtkWidget *window, *button1, *button2, *hpaned;

	gtk_init (&argc, &argv);

	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	gtk_widget_set_size_request (window, 400, 100);

	hpaned = gtk_hpaned_new ();

	button1 = gtk_button_new_with_label ("button 1");
	
	button2 = gtk_button_new_with_label ("button 2");

	gtk_paned_add1 (GTK_PANED (hpaned), button1);
	gtk_paned_add2 (GTK_PANED (hpaned), button2);

	gtk_container_add (GTK_CONTAINER (window), hpaned);

	gtk_widget_show_all (window);

	gtk_main();

	return 0;



};

