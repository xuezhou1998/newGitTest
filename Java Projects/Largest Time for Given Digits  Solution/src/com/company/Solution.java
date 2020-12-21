package com.company;



import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Solution {
    public String largestTimeFromDigits(int[] arr) {
        String result;
        String newDigit="";
        String emptystr="";
        ArrayList<Integer> arr2 =new ArrayList<Integer>();


        for (int i = 0; i < arr.length; i++) {

            int maxdigit= arr[getMax(arr)];
            if (i==0){
                if (maxdigit<=2){
                    newDigit+=Integer.toString(maxdigit);
                    arr2.add(-1);

                }
                else {
                    int choosen=0;
                    int index=0;
                    for ( int j = 0; j < arr.length; j++) {
                        if (arr[j]<=2 && arr[j]>=choosen){
                            choosen=arr[j];
                            index = j;
                        }
                    }
                    newDigit+=Integer.toString(choosen);
                    arr2.add(-1);

                }
            }
            else if(i==1){
                if (maxdigit<=3){
                    newDigit+=Integer.toString(maxdigit);
                    arr2.add(-1);
                    newDigit+=":";
                }
                else {
                    int choosen=0;
                    int index=0;
                    for ( int j = 0; j < arr.length; j++) {
                        if (arr[j]<=3 && arr[j]>=choosen){
                            choosen=arr[j];
                            index = j;
                        }
                    }
                    newDigit+=Integer.toString(choosen);
                    arr2.add(-1);
                    newDigit+=":";
                }




            }
            else if(i==2){
                if (maxdigit<=5){
                    newDigit+=Integer.toString(maxdigit);
                    arr2.add(-1);

                }
                else {
                    int choosen=0;
                    int index=0;
                    for ( int j = 0; j < arr.length; j++) {
                        if (arr[j]<=5 && arr[j]>=choosen){
                            choosen=arr[j];
                            index = j;
                        }
                    }
                    newDigit+=Integer.toString(choosen);
                    arr2.add(-1);
                }




            }
            else {
                newDigit+=Integer.toString(maxdigit);

                arr2.add(-1);
            }
            for (int j = 0; j < arr.length; j++){
                if (arr2.size()!=arr.length){
                    System.out.println(String.format("not completed %d",arr2.size() ));
                    return emptystr;
                }
            }
        }
        return  newDigit;

    }
    public static int getMax(int[] inputArray){
        int maxValue = -1;
        int index=0;
        for( int i=0;i < inputArray.length;i++){
            if(inputArray[i] > maxValue){
                maxValue = inputArray[i];
                index = i;
            }
        }
        return index;
    }

    // Method for getting the minimum value
    public static int getMin(int[] inputArray){
        int minValue = -1;
        int index=0;
        for(int i=0;i<inputArray.length;i++){
            if(inputArray[i] < minValue){
                minValue = inputArray[i];
                index=i;
            }
        }
        return index;
    }
}

