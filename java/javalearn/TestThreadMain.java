/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

/**
 *
 * @author user
 */
public class TestThreadMain 
{
    static void main() 
    {
        System.out.println(Thread.currentThread().getName());
        
        //
        WorkerThread worker = new WorkerThread();
        worker.work(2, 1000, "Hello");
    }   
}
