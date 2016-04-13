#include <gtk/gtk.h>

int main (int argc, char *argv[])
{
	GtkWidget *window, *spin;
	GtkAdjustment *integer;

	gtk_init (&argc, &argv);

	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	gtk_widget_set_size_request (window, 400, 100);

	integer = GTK_ADJUSTMENT (gtk_adjustment_new (5, 1, 10, 1, 2, 2)  );

	spin = gtk_spin_button_new (integer, 1, 0);

	gtk_container_add (GTK_CONTAINER (window), spin);

	gtk_widget_show_all (window);

	gtk_main ();

	return 0;
};

