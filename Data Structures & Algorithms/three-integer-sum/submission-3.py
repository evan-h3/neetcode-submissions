class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        for i, a in enumerate(nums):
            #no need to check positives
            if a > 0:
                break
            #duplicate check
            if i > 0 and a == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1
            while l<r:
                threeSum = a + nums[l] + nums[r]
                if threeSum == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                elif threeSum > 0:
                    r-=1
                else:
                    l+=1

        return ans

