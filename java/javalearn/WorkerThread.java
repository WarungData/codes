/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

/**
 *
 * @author user
 */
public class WorkerThread 
{
    public void work(int n, int delay, String message)
    {
        for (int i=0; i<n; i++)
        {
            System.out.println(message + ":" + i);
            try 
            {
                Thread.sleep(delay);
            } 
            catch (InterruptedException ex) 
            {
                break;
            }
        }
    }
    
    public void workSync(int delay, String message)
    {
        System.out.print("[");
        try 
        {
            Thread.sleep(delay);
        } 
        catch (InterruptedException ex) 
        {
        }
        System.out.print(message);
        System.out.println("]");
    }
    
    //kalau tidak pakai instance kelas ini, bisa pakai method ini
    public static void workStatic(int n, int delay, String message)
    {
        for (int i=0; i<n; i++)
        {
            System.out.println(message + ":" + i);
            try 
            {
                Thread.sleep(delay);
            } 
            catch (InterruptedException ex) 
            {
                break;
            }
        }
    }
}
