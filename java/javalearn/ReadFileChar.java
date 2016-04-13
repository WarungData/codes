/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 *
 * @author user
 */
class ReadFileChar 
{
    static void main() 
    {
        File f = new File(JavaLearn.CURDIR + File.separator + JavaLearn.FNAME);
        
        //
        BufferedReader br = null;
        try 
        {
            br = new BufferedReader(new InputStreamReader(new FileInputStream(f)));
        } 
        catch (FileNotFoundException ex) 
        {
            ex.printStackTrace(System.err);
            return;
        }
        
        //
        String line = null;
        try 
        {
            while (true)
            {
                line = br.readLine();
                
                //
                if (line == null || line.trim().length() < 1)
                {
                    break;
                }
                
                //
                System.out.println(line);
            }
        } 
        catch (IOException ex) 
        {
        }
        
        //
        try 
        {
            br.close();
        } 
        catch (IOException ex) 
        {
            ex.printStackTrace(System.err);
            return;
        }
    }
}
