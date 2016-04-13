/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

/**
 *
 * @author user
 */
class ReadFile 
{
    static void main()
    {
        File f = new File(JavaLearn.CURDIR + File.separator + JavaLearn.FNAME);
        
        //
        FileInputStream fin = null;
        try 
        {
            fin = new FileInputStream(f);
        } 
        catch (FileNotFoundException ex) 
        {
            ex.printStackTrace(System.err);
            return;
        }
        
        //
        int c = -1;
        try 
        {
            c = fin.read();
            while (c != -1)
            {
                System.out.print((char) c);
                c = fin.read();
            }
        } 
        catch (IOException ex) 
        {
        }
        
        //
        try 
        {
            fin.close();
        } 
        catch (IOException ex) 
        {
            ex.printStackTrace(System.err);
            return;
        }
    }
}
