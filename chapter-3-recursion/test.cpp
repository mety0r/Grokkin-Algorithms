bool checkSortedOptimized(int* arr, int n) {
    // code is more readable
    if (n == 1) return true;                                                

    bool prevSorted = checkSortedOptimized(arr, n - 1);                      
    // early return
    if(prevSorted == false) return false;

    // early return
    if(arr[n - 1] < arr[n - 2]) return false;

    return true;
}