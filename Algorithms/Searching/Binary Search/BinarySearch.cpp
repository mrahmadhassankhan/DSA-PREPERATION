#include <iostream>
using namespace std;

int binarySearch(const int array[], int n, int lowerbound, int upperbound)
{
    while (lowerbound <= upperbound)
    {
        int middlepoint = (lowerbound + upperbound) / 2;
        int middlevalue = array[middlepoint];

        if (n == middlevalue)
        {
            return middlepoint; // Return the index of the search value
        }
        else if (n < middlevalue)
        {
            upperbound = middlepoint - 1;
        }
        else
        {
            lowerbound = middlepoint + 1;
        }
    }
    return -1; // Return -1 if the value is not found
}

int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int length = sizeof(arr) / sizeof(arr[0]);
    int upperbound = length - 1;
    int lowerbound = 0;
    int searchValue = 8;

    int index = binarySearch(arr, searchValue, lowerbound, upperbound);

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
