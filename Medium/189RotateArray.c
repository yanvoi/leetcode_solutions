

void rotate(int* nums, int numsSize, int k){
  
    int tab[numsSize];
  
    for(int i = 0; i < numsSize; i++)
    {
        tab[i] = nums[i];
    }
  
    for(int i = 0; i < numsSize; i++)
    {
        nums[(i+k) % numsSize] = tab[i];
    }
}
