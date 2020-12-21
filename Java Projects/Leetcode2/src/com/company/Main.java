package com.company;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Solution testingclass=new Solution();
        int[] inputarray={-2147483648,2147483647};
        boolean testresult = testingclass.containsNearbyAlmostDuplicate(inputarray,1,1);
        System.out.println(testresult);
        int a = 2147483647;
        int b = 2147483647;
        System.out.println(a+b);
    }
}
