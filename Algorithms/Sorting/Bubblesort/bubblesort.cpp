#include <iostream>
using namespace std;
void bubble_sort(int arr[],int n){
    bool sorted = false;
    for (int i = 0;i<n-1 && !sorted;++i){
        sorted = true;
        for(int j=0;j<n-i-1;++j){
            if(arr[j]>arr[j+1]){
                swap(arr[j],arr[j+1]);
                sorted = false;
            }
        }
    }
}
int main(){
int arr[] = {43,23,55,11,23,56,12,999,1,2};
int n = sizeof(arr) / sizeof(arr[0]);
bubble_sort(arr,n);
cout<<"Sorted Array ";
for(int i =0;i<n;++i){
    cout<<arr[i]<<" ";
}
cout<<endl;
return 0;
}