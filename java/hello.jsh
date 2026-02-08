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
System.out.println("human readable time: " + java.time.Instant.now());

/** but writing snippets like this will not teach me about @autowired and fancy IDE highlighting, git cherrypicking etc.! */

/** cut and paste: 
@Autowired is an annotation in Spring Framework that enables dependency injection 
for Java classes. It allows Spring to automatically inject dependencies into the class, 
eliminating the need for manual configuration. This annotation can be used to inject 
dependencies into fields, methods, and constructors.
https://vicksheet.medium.com/understanding-autowired-in-spring-framework-benefits-and-types-5ce8815d99d7
https://stackoverflow.com/questions/67727341/what-exactly-does-autowired-mean-in-java
https://stackoverflow.com/questions/41839723/what-is-the-proper-way-to-do-checkout-with-rebase-and-then-push-the-merged-fil
https://www.jetbrains.com/help/idea/manage-branches.html#checkout-Git-branch
*/ 

/exit
