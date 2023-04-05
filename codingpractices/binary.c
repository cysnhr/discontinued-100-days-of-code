int search(int* nums, int numsSize, int target) {
    
    // initialization
    // set left right bounds
    int left = 0;
    int right = numsSize - 1;
    int mid = numsSize / 2;
    
    while (left <= right) {
        printf("%i %i %i\n", left, right, mid);
        mid = (left + right) / 2;
        if (target > nums[mid]) {
            left = mid + 1;
        }
        else if (target < nums[mid]) {
            right = mid - 1;
        }
        else if (target == nums[mid]) {
            return mid;
        }
    }
    
    return -1;
    
}
