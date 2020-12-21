import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }


}


class Solution {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        int carry = 0;




        return l1;
    }

    public ArrayList<Integer> traverse (ListNode l){
        ArrayList<Integer> listReturn =new ArrayList<Integer>();
        ListNode tmpListNode = l;
        while (tmpListNode.next!= null){
            listReturn.add(tmpListNode.val);
            System.out.println(tmpListNode.val);
            tmpListNode=tmpListNode.next;
        }
        return listReturn;

    }

}




