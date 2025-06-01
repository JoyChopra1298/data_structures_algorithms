/*
Definition of Linear O(n) Time Complexity
An algorithm runs in O(n) time if the number of operations it performs is 
directly proportional to the size of the input n
*/

fn linear_sum(array: &[i32]) -> (i32, usize) {
    let mut sum = 0;
    let mut total_operations = 0;

    // Let n be the size of the input array
    // The sum operation inside the loop takes constant time,
    // and the loop runs 'n' times.
    // Hence the total time is proportional to n
    for &number in array {
        sum += number;
        total_operations += 1;
    }

    (sum, total_operations)
}

// Creates a vector [1, 2, ..., n]
fn create_array(n: usize) -> Vec<i32> {
    (1..=n as i32).collect()
}

fn main() {
    // Test the linear_sum function for arrays of size 1 to 10
    for index in 1..=10 {
        let numbers = create_array(index);
        let (_sum, total_operations) = linear_sum(&numbers);
        println!("n = {}, Operations = {}", index, total_operations);
    }
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
