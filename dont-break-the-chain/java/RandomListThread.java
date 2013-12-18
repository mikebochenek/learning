import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;


/**
 * C:\data\projects\portal_trunk\zoo\src\zoo\mb\threads
 */
public class RandomListThread implements Runnable {

	final static int MAXTHREADS = 10000;//0;
	
	public void run() {
		removeRandomElement(mylist);
		//getRandomElement(mylist);
		getRandomElement(Collections.synchronizedList(mylist));
		
		if (mylist.size() <= 3) {
			mylist = createSomeList();
		}
	}

	public static void main(String[] args) {
		for (int i = 0; i < MAXTHREADS; i++) {
			(new Thread(new RandomListThread(i))).start();
		}
	}
	
	public static List mylist = createSomeList();
	public static List createSomeList() {
		List list = new ArrayList();
		for (int i = 0; i < 100; i++) {
			list.add(i);
		}
		return list;
	}
	
	private int id;
	public RandomListThread(int i) {
		id = i;
	}
	
	public Object getRandomElement(List list) {
		Random r = new Random();
		int idx = r.nextInt(list.size());
		return list.get(idx);
	}
	
	public void removeRandomElement(List list) {
		Random r = new Random();
		int idx = r.nextInt(list.size());
		list.remove(idx);
	}
}
