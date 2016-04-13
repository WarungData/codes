/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 *
 * @author user
 */
public class JavaLearn 
{

    /**
     * @param args the command line arguments
     */
    public static final String FNAME = "test.txt";
    public static final String CURDIR = System.getProperty("user.dir");
    
    //DB related only (point f)
    public static final String DBNAME = "InMemoryDatabase";
    public static final String DBCONN = "jdbc:derby:memory:" + DBNAME + ";create=true";
    public static final String DBDRIVER = "org.apache.derby.jdbc.EmbeddedDriver";
    
    
    public static void main(String[] args) 
    {
        System.out.println("Menu");
        System.out.println("----");
        System.out.println("1. [" + CURDIR + "] Isi direktori aktif");
        System.out.println("2. [" + FNAME +  "] Buat file");
        System.out.println("3. [" + FNAME +  "] Hapus file");
        System.out.println("4. [" + FNAME +  "] (Stream) Tulis file");
        System.out.println("5. [" + FNAME +  "] (Stream) Baca file");
        System.out.println("6. [" + FNAME +  "] (Char) Tulis file");
        System.out.println("7. [" + FNAME +  "] (Char) Baca file");
        System.out.println("8. Thread utama");
        System.out.println("9. Thread satu");
        System.out.println("a. Thread multi");
        System.out.println("b. Thread sync");
        System.out.println("c. Thread join");
        System.out.println("d. Thread stop");
        System.out.println("e. GUI");
        System.out.println("f. [" + DBNAME +  "] Database");
        System.out.println("g. Load jar");
        
        //
        System.out.print("Masukkan pilihan: ");
       
        //
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        String input = null;
        try 
        {
            input = br.readLine().trim();
        } 
        catch (IOException ex) 
        {
            ex.printStackTrace(System.err);
        }
        
        //
        processInput(input);
    }

    private static void processInput(String input) 
    {
        if (input.equals("1"))
        {
            ListDir.main();
        }
        else
        if (input.equals("2"))
        {
            CreateFile.main();
        }
        else
        if (input.equals("3"))
        {
            DeleteFile.main();
        }
        else
        if (input.equals("4"))
        {
            WriteFile.main();
        }
        else
        if (input.equals("5"))
        {
            ReadFile.main();
        }        
        else
        if (input.equals("6"))
        {
            WriteFileChar.main();
        }
        else
        if (input.equals("7"))
        {
            ReadFileChar.main();
        }
        else
        if (input.equals("8"))
        {
            TestThreadMain.main();
        }
        else
        if (input.equals("9"))
        {
            TestThreadSingle.main();
        }
        else
        if (input.equals("a"))
        {
            TestThreadMulti.main();
        }
        else
        if (input.equals("b"))
        {
            TestThreadSync.main();
        }
        else
        if (input.equals("c"))
        {
            TestThreadJoin.main();
        }
        else
        if (input.equals("d"))
        {
            TestThreadStop.main();
        }
        else
        if (input.equals("e"))
        {
            GUI.main();
        }
        else
        if (input.equals("f"))
        {
            Database.main();
        }
        else
        if (input.equals("g"))
        {
            LoadJar.main();
        }
    }
}