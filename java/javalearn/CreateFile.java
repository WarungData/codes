/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

import java.io.File;
import java.io.IOException;

/**
 *
 * @author user
 */
public class CreateFile 
{
    static void main() 
    {
        System.out.println("Membuat File " + JavaLearn.FNAME);
        
        //
        File f = new File(JavaLearn.CURDIR + File.separator + JavaLearn.FNAME);
        
        //
        boolean res = false;
        try 
        {
            res = f.createNewFile();
        } 
        catch (IOException ex) 
        {
            ex.printStackTrace(System.err);
        }
        
        //
        if (res)
        {
            System.out.println("OK");
        }
        else
        {
            System.out.println("FAILED");
        }
    }
}
