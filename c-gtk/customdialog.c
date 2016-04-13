#include <gtk/gtk.h>

int main (int argc, char *argv[])
{
	GtkWidget *dialog, *table, *nama, *alamat, *pekerjaan;

	GtkWidget *lbl1, *lbl2, *lbl3;

	gint result;

	gtk_init (&argc, &argv);

	dialog = gtk_dialog_new_with_buttons ("Edit informasi", NULL, GTK_DIALOG_MODAL, GTK_STOCK_OK, GTK_RESPONSE_OK, GTK_STOCK_CANCEL, GTK_RESPONSE_CANCEL, NULL);

	gtk_dialog_set_default_response (GTK_DIALOG (dialog), GTK_RESPONSE_OK);

	lbl1 = gtk_label_new ("Nama:");
	lbl2 = gtk_label_new ("Alamat");
	lbl3 = gtk_label_new ("Pekerjaan");

	nama = gtk_entry_new ();
	alamat = gtk_entry_new ();
	pekerjaan = gtk_entry_new ();

	table = gtk_table_new (4, 2, FALSE);
	gtk_table_attach_defaults (GTK_TABLE (table), lbl1, 0, 1, 0, 1);
	gtk_table_attach_defaults (GTK_TABLE (table), lbl2, 0, 1, 1, 2);
	gtk_table_attach_defaults (GTK_TABLE (table), lbl3, 0, 1, 2, 3);
	gtk_table_attach_defaults (GTK_TABLE (table), nama, 1, 2, 0, 1);
	gtk_table_attach_defaults (GTK_TABLE (table), alamat, 1, 2, 1, 2);
	gtk_table_attach_defaults (GTK_TABLE (table), pekerjaan, 1, 2, 2, 3);


	gtk_table_set_row_spacings (GTK_TABLE (table), 5);
	gtk_table_set_col_spacings (GTK_TABLE (table), 5);

	gtk_box_pack_start_defaults (GTK_BOX (GTK_DIALOG (dialog) -> vbox), table);

	gtk_widget_show_all (dialog);

	result = gtk_dialog_run (GTK_DIALOG (dialog));
	if (result == GTK_RESPONSE_OK)
	{
		g_print ("OK\n");
	}
	else
	if (result == GTK_RESPONSE_CANCEL)
	{

		g_print ("CANCEL\n");
	}

	gtk_widget_destroy (dialog);
	return 0;
};

