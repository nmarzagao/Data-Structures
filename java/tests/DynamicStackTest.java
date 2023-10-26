import com.datastructures.Node;
import com.datastructures.DynamicStack;

/* 
To compile this code:
cd root
javac -d . com/datastructures/Node.java com/datastructures/DynamicStack.java tests/DynamicStackTest.java 
java DynamicStackTest 
*/

// Dynamic stack is working, I just have to write the unit testing code and gg


class DynamicStackTest {

    public static void main(String[] args) {
        DynamicStack s = new DynamicStack(new Node("First"));

        s.push(new Node("Second!"));
        s.push(new Node("Third!"));

        s.pop();

        print_stack(s.getTop());
        
    }

    public static void print_stack(Node s) {
        if (s == null) {
            return;
        }
        else {
            System.out.println(s.getVal());
            print_stack(s.getNext());
        }
    }
}