#include <vector>
#include <algorithm>
using namespace std;
class Solution {
private:
    int binary(vector<int>& nums, int val, int left, int right){
        if (val > nums[right])
            return -1;
        int mid;
        while (left < right){
            mid = int(left+right)/2;
            if (nums[mid]>=val)
                right = mid;
            else
                left = mid + 1;
        }
        return right;
    }

public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        if(nums.size() < 3)
            return result;
        int len = nums.size();
        sort(nums.begin(), nums.end());
        vector<int> item;
        int nneg_start = this->binary(nums, 0, 0, len-1);
        if (nneg_start+2 < len && nums[nneg_start]==nums[nneg_start+2] && nums[nneg_start]==0){
            item.clear();
            item.push_back(0);
            item.push_back(0);
            item.push_back(0);
            result.push_back(item);
        }

        for(int i=0;i<nneg_start;i++){
            if (!i || nums[i]!=nums[i-1]){
                int n_i = -nums[i];
                int k_left, k_right, j_left, j_right;
                if(nums[len-1] >= 2*n_i){
                    k_right = this->binary(nums, 2*n_i, nneg_start, len-1);
                    k_left = this->binary(nums, int(n_i/2), nneg_start, k_right);
                    j_right = k_left;
                    j_left = i+1;
                }
                else if(nums[len-1] >= n_i){
                    k_right = len-1;
                    k_left = this->binary(nums, int(n_i/2), nneg_start, k_right);
                    j_right = k_left;
                    j_left = this->binary(nums, n_i-nums[len-1], i+1, nneg_start);
                }
                else if(nums[len-1] >= int(n_i/2)){
                    k_right = len-1;
                    k_left = this->binary(nums, int(n_i/2), nneg_start, k_right);
                    j_right = k_left;
                    j_left = this->binary(nums, n_i-nums[len-1], nneg_start, j_right);
                }
                else
                    continue;
                if(j_left == k_right)
                    continue;
                if(nums[k_left]==int(n_i/2) && k_left!=k_right)
                    k_left += 1;

                for(int j=j_left;j<j_right+1;j++){
                    if(j==j_left || nums[j]!=nums[j-1]){
                        int k = this->binary(nums, -(nums[i]+nums[j]), k_left, k_right);
                        if(k!=-1 && nums[i]+nums[j]+nums[k]==0){
                            item.clear();
                            item.push_back(nums[i]);
                            item.push_back(nums[j]);
                            item.push_back(nums[k]);
                            result.push_back(item);
                        }
                    }
                }
            }
        }
        return result;
    }
};
