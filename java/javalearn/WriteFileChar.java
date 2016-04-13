/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;

/**
 *
 * @author user
 */
class WriteFileChar 
{
    static void main() 
    {
        File f = new File(JavaLearn.CURDIR + File.separator + JavaLearn.FNAME);
        
        //
        BufferedWriter bw = null;
        try 
        {
            bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(f)));
        } 
        catch (FileNotFoundException ex) 
        {
            ex.printStackTrace(System.err);
            return;
        }
        
        //
        for (int i=0; i<5; i++)
        {
            String line = "Baris ke " + i;
            try 
            {
                bw.write(line);
                bw.newLine();
            } 
            catch (IOException ex) 
            {
                break;
            }
        }
        
        //
        try 
        {
            bw.close();
        } 
        catch (IOException ex) 
        {
            ex.printStackTrace(System.err);
            return;
        }
    }
}
