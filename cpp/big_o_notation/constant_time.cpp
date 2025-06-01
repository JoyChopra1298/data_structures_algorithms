/*
Definition of Constant O(1) Time Complexity
An algorithm runs in O(1) time if the number of operations it performs is 
independent of the size of the input n
*/

#include <iostream>
#include <vector>

std::pair<int, int> head(const std::vector<int>& array) {
    int total_operations = 0;

    // The operation to access the first element of the array is constant time
    int head_element = array[0]; // Constant time operation
    total_operations += 1;

    return {head_element, total_operations};
}

// This function creates a vector [1, 2, ..., n]
std::vector<int> create_array(int n) {
    std::vector<int> vector1;
    for (int index = 1; index <= n; index++) {
        vector1.push_back(index);
    }
    return vector1;
}

int main() {
    // Test the head function for arrays of increasing size from 1 to 10
    for (int index = 1; index <= 10; index++) {
        std::vector<int> numbers = create_array(index);
        auto [sum, total_operations] = head(numbers);
        std::cout << "n = " << index << ", Operations = " << total_operations << std::endl;
    }
    return 0;
}

/*
Output:

n = 1, Operations = 1
n = 2, Operations = 1
n = 3, Operations = 1
n = 4, Operations = 1
n = 5, Operations = 1
n = 6, Operations = 1
n = 7, Operations = 1
n = 8, Operations = 1
n = 9, Operations = 1
n = 10, Operations = 1
*/
