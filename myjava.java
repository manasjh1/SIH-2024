// Java Program to Delete an element
// from a specific position in a Sorted Array
class myjava {
    static void InsertionSort(int[] arr,int n) {
       for(int i=0;i<n;i++){
        int key=arr[i];
        int j=i-1;
        while(j>=0&&arr[j]>key){
            arr[j+1]=arr[j];
            j=j-1;
        }
        arr[j+1]=key;
       }
        
    }
    static void printArray(int arr[],int n){
        for(int i=0;i<n;i++){
            System.out.println(arr[i]+" ");
        }
    }
    public static void main(String[] args) {
        int arr[] = {66,20,14,5,8}; // Array with enough capacity
       // Initial sorted elements
        int n=arr.length;
        InsertionSort(arr, n);
        System.out.println("Sorted array is done by bubble sort");
        printArray(arr, n);
        
    }
}

// This code is contributed by syedsarfarazahammed
