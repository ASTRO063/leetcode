#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n=nums.size();
        
        vector<int> left,right,res;
        left.assign(n+1,0);
        right.assign(n+1,0);
        res.assign(n,0);
        
        
        //left product array's first element is initialised as 1
        //right product array's last element is initialised as 1
        left[0]=1;
        right[n]=1;

        //calculating left product array
        // for(int i=1;i<=n;i++){
        //     left[i]=left[i-1]*nums[i-1];            
        // }
        //printing left product array
        // cout<<"\nleft \n";
        // for(int i=0;i<=n;i++){  
        //     cout<<left[i]<<" ";
        //  }
        
        //calculating right product array
        // for(int i=n-1;i>=0;i--){
        // //  cout<<"i="<<i<<" value ="<<nums[i]<<" right ="<<right[i+1]<<"\n";
        //     right[i]=nums[i]*right[i+1];
        // // cout<<"\n righ="<<right[i]<<"\n";
        // }
        //printing right product array
        // cout<<"\n right\n";
        // for(int i=0;i<n;i++){      
        //  cout<<right[i]<<" ";
        //}
        
        
        //writing above two calcutions in one loop
        for(int i=1;i<=n;i++){
            left[i]=left[i-1]*nums[i-1];
            right[n-i]=right[n-i+1]*nums[n-i];
        }
    
        for(int i=0;i<n;i++){
           
           res[i]=left[i]*right[i+1];
        }
        
        return res;
    }
    
};
