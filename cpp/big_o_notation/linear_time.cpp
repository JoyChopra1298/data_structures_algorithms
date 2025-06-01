/*
Definition of Linear O(n) Time Complexity
An algorithm runs in O(n) time if the number of operations it performs is 
directly proportional to the size of the input n
*/

#include <iostream>
#include <vector>

std::pair<int, int> linear_sum(const std::vector<int>& array) {
    int sum = 0;
    int total_operations = 0;

    // Let n be the size of the input array
    // The sum operation inside the loop takes constant time,
    // and the loop runs 'n' times.
    // Hence the total time is proportional to n
    for (int number : array) {
        sum += number;       // Constant time operation
        total_operations++;
    }
    return {sum, total_operations};
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
    // Test the linear_sum function for arrays of increasing size from 1 to 10
    for (int index = 1; index <= 10; index++) {
        std::vector<int> numbers = create_array(index);
        auto [sum, total_operations] = linear_sum(numbers);
        std::cout << "n = " << index << ", Operations = " << total_operations << std::endl;
    }
    return 0;
}

/*
Output:

n = 1, Operations = 1
n = 2, Operations = 2
n = 3, Operations = 3
n = 4, Operations = 4
n = 5, Operations = 5
n = 6, Operations = 6
n = 7, Operations = 7
n = 8, Operations = 8
n = 9, Operations = 9
n = 10, Operations = 10
*/
