#include <stdio.h>


//A unility function to swap two element 
void swap(int* a, int* b){
    int temp = *a; 
    *a = *b; 
    *b = temp; 
}

/*This function takes last element as pivot, places 
the pivot element at its correct position in sorted 
array, and places all smaller(smaller than pivot)
to left of pivot and all greater elements to right
of pivot 
*/

int partition(int arr[], int low, int high){
    int pivot = arr[high]; //this is the pivot 
    int i = (low-1); //Index of smaller element
    int j;  

    for(int j = low; j<=high-1; j++){
        //If the current element is smaller than or 
        //equal to pivot
        if(arr[j]<=pivot){
            i++; //increment index of smaller element
            swap(&arr[i], &arr[j]); 
        }
    }
    swap(&arr[i+1],&arr[high]); 
    return i+1; 
}

void 
quickSort(int arr[], int low, int high){
    if(low<high){
        /*pi is partition index, arr[p] is 
        at the right place */
        int pi = partition(arr, low, high); 

        //Separately sort elements before 
        // partition and after partition 
        quickSort(arr, low, pi-1); //smaller than pi
        quickSort(arr, pi+1, high); //bigger than pi
    }
}

/*function to print an array */

void 
printArray(int arr[], int size){
    int i; 
    for(i=0; i<size; i++){
        printf("%d ", arr[i]); 
    }
    printf("\n"); 
}


int findContentChildren(int* g, int gSize, int* s, int sSize){
    /*sort two arrays first, time complexity is 2*O(nlogn) */
    //children array
    quickSort(g, 0, gSize-1); 
    //cookies array
    quickSort(s, 0, sSize-1); 
    
    /*count the number of child that can be satisfied*/
    int num = 0; 
    int childcounter = 0; 
    int cookiecounter = 0; 
    while (childcounter<gSize && cookiecounter<sSize){
        if(g[childcounter]<=s[cookiecounter]){
            childcounter++; 
            num++; 
        }
        cookiecounter++;
    }
    return num; 
}


