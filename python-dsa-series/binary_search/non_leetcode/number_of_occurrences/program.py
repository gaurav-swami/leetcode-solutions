class Solution:
    def countFreq(self, arr, target):
        lb = self.lower_bound(arr,target)
        if lb == -1:
            return 0
        return self.upper_bound(arr,target) - lb
        
            
        # code here
        
    def lower_bound(self,arr,target):
        l,r = 0,len(arr)-1
        lb = -1
        while l<=r:
            m = l + (r-l)//2
            if arr[m]>=target:
                lb = m
                r = m- 1
            else:
                l = m + 1
                
        return lb
        
    def upper_bound(self,arr,target):
        l,r = 0,len(arr)-1
        ub = len(arr)
        while l<=r:
            m = l + (r-l)//2
            
            if arr[m]>target:
                ub = m
                r = m - 1
            else:
                l = m + 1
                
        return ub
        
