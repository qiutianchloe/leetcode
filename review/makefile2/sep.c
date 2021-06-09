int find_max(int arr[], int length){
    int max = arr[0]; 
    int i; 
    for(i=0; i<length; i++){
        if (arr[i]>max){
            max = arr[i]; 
        }
    }
    return max; 
}