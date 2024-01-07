import math 

class RadixSort():
    """
    RadixSort implementation with callback for array structure changes.
    """
    def __init__(self):
        pass

    def sort(self, values, callback=None):
        if values is None: 
            return
        return self.radixSort(values, callback)

    def getMax(self, array):
        maxNum = array[0]
        for i in range(0, len(array)):
            if array[i] > maxNum:
                maxNum = array[i]
        return maxNum

    def calculateNumberOfDigits(self, number):
        return int(math.log(number, 10) + 1)

    def radixSort(self, numbers, callback=None):
        if numbers is None or len(numbers) <= 1:
            return numbers

        maximum = self.getMax(numbers)
        numberOfDigits = self.calculateNumberOfDigits(maximum)
        placeValue = 1

        while numberOfDigits > 0:
            numberOfDigits -= 1
            numbers = self.countSort(numbers, placeValue, callback)
            placeValue *= 10
            
        return numbers

    def countSort(self, numbers, placeValue, callback=None):
        rangeParm = 10
        frequency = [0] * rangeParm
        sortedValues = [None] * len(numbers)

        for i in range(0, len(numbers)):
            digit = (numbers[i] // placeValue) % rangeParm
            frequency[digit] += 1

        for i in range(1, rangeParm):
            frequency[i] += frequency[i - 1]

        for i in range(len(numbers) - 1, -1, -1):
            digit = (numbers[i] // placeValue) % rangeParm
            sortedValues[frequency[digit] - 1] = numbers[i]
            frequency[digit] -= 1

        if callback:
            callback(sortedValues)  # Signal array structure changes
        return sortedValues[:len(numbers)]


if __name__ == '__main__':
    """
    Example usage
    """
    def array_structure_changed_callback(arr):
        print(f"Array structure changed: {arr}")

    sorter = RadixSort()
    numbers = [387, 468, 134, 123, 68, 221, 769, 37, 7, 890, 1, 587]

    # Sorting with callback
    numbers = sorter.sort(numbers, array_structure_changed_callback)
    # Prints the sorted array
    print(numbers)
