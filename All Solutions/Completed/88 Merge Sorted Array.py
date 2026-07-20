nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3

for i in range(m,m+n):
    nums1[i] = nums2[i-m]

n = len(nums1)
for i in range(len(nums1)-1):
    for j in range(n-1):
        if nums1[j] > nums1[j+1]:
            temp = nums1[j]
            nums1[j] = nums1[j+1]
            nums1[j+1] = temp
    n -= 1
print(nums1)