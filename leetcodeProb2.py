x=[2,7,11,15]
def twoSum(nums, target):
        if len(nums)<2:
            return None
        seen=[]
        a=[]
        for i in nums:
            t=target-i
            if t not in seen:
                seen.append(i)
            else:
                j=t
                k=i
        for i in range(len(nums)):
            if t==nums[i] or k==nums[i]:
                a.append(i)

        return a
print(twoSum(x,9))

