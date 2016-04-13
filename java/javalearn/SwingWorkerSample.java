/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

import java.util.List;
import java.util.concurrent.ExecutionException;
import javax.swing.JButton;
import javax.swing.JTextField;
import javax.swing.SwingWorker;

/**
 *
 * @author user
 */
//Long pertama adalah kembalian doInBackground dan get
//Long kedua adalah untuk publish dan progress
//coba lihat lagi dokumentasi SwingWorker
public class SwingWorkerSample extends SwingWorker<Long, Long>
{
    private JTextField text;
    private JButton button;
    private int max;
    
    SwingWorkerSample(int max, JTextField text, JButton button)
    {
        this.text = text;
        this.button = button;
        this.max = max;
    }
    
    @Override
    //akan dikerjakan di thread worker, tidak membuat GUI beku
    protected Long doInBackground() throws Exception
    {
        long result = 0;  //hasil perhitungan
        int percent = 0;  //sudah berapa persen? 
        
        for (int i=0; i<max; i++)
        {
            result += i;  //jumlahkan setiap perulangan ke result
            
            percent = (int) ((i/(float)max) * 100)  ; //hitung persentase selesai
            setProgress(percent); //kirim persentase, lihat dokumentasi SwingWorker
            
            publish(result);  //publikasikan result sementara, akan membuat process() dipanggil di EDT, lihat dok SwingWorker
          
            //jika di cancel, maka kita keluar
            if (isCancelled())
            {
                break;
            }
        }
        return new Long(result);
    }
    
    //akan dikerjakan SETELAH doInBackground() selesai, di EDT (Jadi boleh akses komponen GUI)
    //dapatkan hasil dari doInBackground() dengan fungsi get()
    //lihat dokumentasi SwingWorker
    protected void done()
    {
        try
        {
            text.setText("SELESAI: " + get().toString());
            button.setEnabled(true);
        } catch (InterruptedException ex)
        {
            text.setText("ERROR");
        } catch (ExecutionException ex)
        {
            text.setText("ERROR");
        }
    }
    
    //akan dikerjakan di EDT, jadi bebas akses GUI
    //menerima hasil yang dikirim oleh publish() (lihat doInBackground() di atas)
    //
    //perhatikan bahwa publish() yang terlalu sering bisa saja dikirim jadi satu dalam bentuk list
    //publish(1)
    //publish(2)
    //publish(3)
    //--bisa saja dikirim sebagai publish(1, 2, 3)
    protected void process(List<Long> list)
    {
        Long last = list.get(list.size()-1);
        text.setText(last.toString());
    }
}
