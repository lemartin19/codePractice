package coding;
import static org.junit.Assert.*;

import org.junit.Test;

public class ReverseStringTest {

	@Test
	public void test1() {
		ReverseString myReverse = new ReverseString();
		assertTrue(myReverse.reverse("a,b$c").equals("c,b$a"));
	}
	
	@Test
	public void test2(){
		ReverseString myReverse = new ReverseString();
		assertTrue(myReverse.reverse("Ab,c,de!$").equals("ed,c,bA!$"));
	}

}
