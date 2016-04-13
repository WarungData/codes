#include <gtk/gtk.h>

int main (int argc, char *argv[])
{
	GtkWidget *window, *label1, *expander;

	gtk_init (&argc, &argv);

	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	gtk_widget_set_size_request (window, 400, 100);

	label1 = gtk_label_new ("Baris1\nBaris2\nBaris3");

	expander = gtk_expander_new_with_mnemonic ("_Detail");

	gtk_container_add (GTK_CONTAINER (expander), label1);

	gtk_expander_set_expanded (GTK_EXPANDER (expander), TRUE);

	gtk_container_add (GTK_CONTAINER (window), expander);

	gtk_widget_show_all (window);

	gtk_main ();

	return 0;
};

