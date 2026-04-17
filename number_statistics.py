"""
A program to calculate various statistics on a list of numbers.
Contains loops and conditional branches for data processing.
"""

class NumberStatistics:
    """Class to calculate statistics on a list of numbers."""
    
    def __init__(self, numbers):
        """Initialize with a list of numbers."""
        self.numbers = numbers
    
    def get_sum(self):
        """
        Calculate the sum of all numbers using a loop.
        
        Returns:
            int: The sum of all numbers
        """
        total = 0
        # Loop through all numbers
        for num in self.numbers:
            total += num
        return total
    
    def get_max(self):
        """
        Find the maximum number using a loop and conditional branch.
        
        Returns:
            int: The maximum number, or None if list is empty
        """
        # Conditional branch - check if empty
        if len(self.numbers) == 0:
            return None
        
        max_num = self.numbers[0]
        # Loop to find maximum value
        for i in range(1, len(self.numbers)):
            # Conditional branch
            if self.numbers[i] > max_num:
                max_num = self.numbers[i]
        return max_num
    
    def get_min(self):
        """
        Find the minimum number using a loop and conditional branch.
        
        Returns:
            int: The minimum number, or None if list is empty
        """
        # Conditional branch - check if empty
        if len(self.numbers) == 0:
            return None
        
        min_num = self.numbers[0]
        # Loop to find minimum value
        for i in range(1, len(self.numbers)):
            # Conditional branch
            if self.numbers[i] < min_num:
                min_num = self.numbers[i]
        return min_num
    
    def get_average(self):
        """
        Calculate the average of all numbers.
        
        Returns:
            float: The average, or 0 if list is empty
        """
        # Conditional branch
        if len(self.numbers) == 0:
            return 0.0
        return sum(self.numbers) / len(self.numbers)
    
    def count_greater_than(self, threshold):
        """
        Count how many numbers are greater than a threshold.
        Uses loop and conditional branch.
        
        Args:
            threshold (int): The threshold value
            
        Returns:
            int: Count of numbers greater than threshold
        """
        count = 0
        # Loop through all numbers
        for num in self.numbers:
            # Conditional branch
            if num > threshold:
                count += 1
        return count
    
    def is_even_all(self):
        """
        Check if all numbers are even.
        Uses loop and conditional branch.
        
        Returns:
            bool: True if all numbers are even, False otherwise
        """
        # Loop through all numbers
        for num in self.numbers:
            # Conditional branch
            if num % 2 != 0:
                return False
        return True


def main():
    """Main function to demonstrate the NumberStatistics class."""
    numbers = [5, 10, 3, 8, 15, 2, 9]
    stats = NumberStatistics(numbers)
    
    print(f"Numbers: {numbers}")
    print(f"Sum: {stats.get_sum()}")
    print(f"Max: {stats.get_max()}")
    print(f"Min: {stats.get_min()}")
    print(f"Average: {stats.get_average():.2f}")
    print(f"Count > 7: {stats.count_greater_than(7)}")
    print(f"All even: {stats.is_even_all()}")


if __name__ == "__main__":
    main()
