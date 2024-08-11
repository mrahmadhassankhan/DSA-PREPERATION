#include <iostream>
using namespace std;

int linearSearch(const int array[], int n, int length)
{
    for (int i = 0; i < length; i++)
    {
        if (array[i] == n)
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int length = sizeof(arr) / sizeof(arr[0]);
    int searchValue = 5;

    int index = linearSearch(arr, searchValue, length);
    if (index != -1)
    {
        cout << "Value " << searchValue << " found at index: " << index << endl;
    }
    else
    {
        cout << "Value " << searchValue << " not found in the array." << endl;
    }

    return 0;
}
