// # 371- https://leetcode.com/problems/sum-of-two-integers/

class Solution {
    public int getSum(int a, int b) {
        int sol = (a ^ b) ;
        int carry = (a & b) << 1;
        while (carry != 0) {
            int newCarry = (sol & carry) << 1;
            sol = sol  ^ carry;
            carry = newCarry;
        }
        return sol;
    }
}