class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        my_list = []
        for i in range(len(nums)):
            new_list =  [num for j, num in enumerate(nums) if j != i]
            my_num = 1
            for j in range(len(new_list)):
                my_num *= new_list[j]
            my_list.append(my_num)
        return my_list