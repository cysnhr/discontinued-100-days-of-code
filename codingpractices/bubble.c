/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>
#include <math.h>

void swap(int* num1, int* num2);

int* sortedSquares(int* nums, int numsSize, int* returnSize){
    
    int* newNums = (int*)malloc(sizeof(int) * numsSize); //ChatGPT also wrote this line. I'm going to figure out pointers ahhhh
    int counter = 1;
    
    // squaring
    for (int i = 0; i < numsSize; i++) {
        newNums[i] = pow(nums[i], 2);
    }
    
    // bubble sort
    while (counter != 0) {
        counter = 0;
        for (int i = 0; i < numsSize - 1; i++) {
            if (newNums[i] > newNums[i+1]) {
                swap(&newNums[i], &newNums[i+1]);
                counter++;
            }
        }

    }
    
    *returnSize = numsSize;  //ChatGPT wrote this line
    return newNums;
}

void swap(int* num1, int* num2) {
    
    int tmp = *num1;
    *num1 = *num2;
    *num2 = tmp;
    
}
