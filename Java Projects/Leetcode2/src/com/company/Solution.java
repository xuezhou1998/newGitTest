package com.company;


class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        boolean result=false;
        int firstNumber;
        int secondNumber;



        for (int i = 0; i < nums.length; i++) {
            firstNumber=nums[i];
            for (int j = i; j < Math.min(i+k,nums.length); j++) {
                if (j>i && j-i<=k){
                    secondNumber=nums[j];
                    if (firstNumber<0 && secondNumber==2147483647){
                        return false;
                    }
                    else if (firstNumber>0 && secondNumber==-2147483648){
                        return false;
                    }
                    else if (firstNumber==-2147483648 && secondNumber>0){
                        return false;
                    }
                    else if (firstNumber==2147483647 && secondNumber<0){
                        return false;
                    }
                    int difference = Math.abs(firstNumber-secondNumber);

                    if (difference<=t){
                        return true;
                    }
                }


            }

        }

        return result;
    }
}