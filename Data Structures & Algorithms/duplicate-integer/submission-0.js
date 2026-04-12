class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const numsTable = {};

        for (const i of nums) {

            if (i in numsTable) {
                return true;
            } else {
                numsTable[i] = 1;
            }
        }

        return false;
    }
}
