/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

/**
 *
 * @author user
 */
public class TestThreadSingle 
{
    static class ThreadSingle extends Thread
    {
        private WorkerThread worker;
        
        public ThreadSingle(WorkerThread worker) 
        {
            this.worker = worker;
        }
        
        public void run()
        {
            worker.work(3, 1000, Thread.currentThread().getName());
        }
    }
    
    static void main() 
    {
        WorkerThread worker = new WorkerThread();
        
        //
        ThreadSingle t = new ThreadSingle(worker);
        t.setName("MyThread");
        t.start();
        
        //
        for (int i=0; i<5; i++)
        {
            System.out.println(Thread.currentThread().getName() + ":" + i);
            try 
            {
                Thread.sleep(400);
            } 
            catch (InterruptedException ex) 
            {
                break;
            }
        }
    }
}
