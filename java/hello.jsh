/* https://stackoverflow.com/questions/2531938/java-thread-example
 * Posted by Phil - Retrieved 2025-11-21, License - CC BY-SA 2.5 */
public class MyThread extends Thread {
   private int startIdx, nThreads, maxIdx;
   public MyThread(int s, int n, int m) {
      this.startIdx = s;
      this.nThreads = n;
      this.maxIdx = m;
   }

   @Override
   public void run()  {
      for(int i = this.startIdx; i < this.maxIdx; i += this.nThreads) {
         System.out.println("[Thread ID : " + this.getId() + "] i=" + i);
         try {
            Thread.sleep((long)(Math.random() * 10));

         } catch (InterruptedException ie) {}
      }
   }
}

MyThread t1 = new MyThread(0, 3, 9);
MyThread t2 = new MyThread(1, 1, 6);

t1.start();
t2.start(); 

System.out.println("minimal hello! at currentTimeMillis=" + System.currentTimeMillis());

/** but writing snippets like this will not teach me about @autowired and fancy IDE highlighting, git cherrypicking etc.! */

/exit
