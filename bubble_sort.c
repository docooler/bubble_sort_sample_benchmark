#include <stdio.h>
#define LEN 20

void bubble_sort(int arr[], int length)
{
    int tmp;
    int i ;
    int j;

    for (i = 0; i < length-1; ++i)
    {
    	for ( j = i+1; j < length; ++j)
    	{
    		if (arr[j] < arr[i])
    		{
    			tmp    = arr[i];
    			arr[i] = arr[j];
    			arr[j] = tmp; 
    		}
    	}
    }
}

int  main(void)
{
	int array[] = {4, 88, 5, 21, 92, 37, 56, 13, 75, 19, 64, 57, 94, 34, 8, 12, 71, 99, 102, 38};
	bubble_sort(array, LEN);
	return 0;
}
