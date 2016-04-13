/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

import java.io.File;
import java.text.NumberFormat;
import java.util.Formatter;

/**
 *
 * @author user
 */
public class ListDir 
{
    static void main() 
    {
        File f = new File(".");
        String[] flist = f.list();
        for (int i=0; i<flist.length; i++)
        {
            File fi = new File(JavaLearn.CURDIR + File.separator + flist[i]);
            if (fi.isDirectory())
            {
                System.out.print("[DIR ]");
            }
            else
            {
                System.out.print("[    ]");
            }
            
            
            //
            System.out.print("[");
            if (fi.canRead())
            {
                System.out.print("r");
            }
            else
            {
                System.out.print("-");
            }
            //
            if (fi.canWrite())
            {
                System.out.print("w");
            }
            else
            {
                System.out.print("-");
            }
            System.out.print("]");
            
            //
            String filen = NumberFormat.getInstance().format(fi.length());
            StringBuilder sb = new StringBuilder();
            Formatter form = new Formatter(sb);
            form.format("%10s", filen);
            System.out.print("[" + sb + "]");
            
            //
            System.out.println(flist[i]);            
        }
    }   
}