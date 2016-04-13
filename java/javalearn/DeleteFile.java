/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

import java.io.File;

/**
 *
 * @author user
 */
public class DeleteFile 
{
    static void main() 
    {
        System.out.println("Menghapus file " + JavaLearn.FNAME);
        
        //
        File f = new File(JavaLearn.CURDIR + File.separator + JavaLearn.FNAME);
        
        //
        boolean res = f.delete();
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
