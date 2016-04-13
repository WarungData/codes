/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;

/**
 *
 * @author user
 */
class WriteFile 
{
    static void main() 
    {
        File f = new File(JavaLearn.CURDIR + File.separator + JavaLearn.FNAME);
        
        //
        FileOutputStream fout = null;
        try 
        {
            fout = new FileOutputStream(f);
        } 
        catch (IOException ex) 
        {
            System.err.println(ex.getMessage());
            return;
        }
        
        //
        String line = "Hello World";
        for (int j=0; j<line.length(); j++)
        {
            try 
            {
                fout.write((int) line.charAt(j));
            }
            catch (IOException ex) 
            {
                break;
            }
        }
        
        //
        try 
        {
            fout.close();
        } 
        catch (IOException ex) 
        {
            ex.printStackTrace(System.err);
            return;
        }   
    }
}