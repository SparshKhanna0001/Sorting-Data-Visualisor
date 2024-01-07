import sys

class BucketSort():
    def __init__(self, callback=None):
        self.callback = callback

    def notify_array_modified(self):
        if self.callback:
            self.callback()

    def sort(self, values):
        minValue = sys.maxsize
        maxValue = -sys.maxsize - 1
        for i in range(len(values)):
            if values[i] < minValue:
                minValue = values[i]
            if values[i] > maxValue:
                maxValue = values[i]

        self.bucketSort(values, minValue, maxValue)

    def bucketSort(self, ar, minValue, maxValue, numBuckets=10):
        # Initialize buckets list
        buckets = [[] for _ in range(numBuckets)]

        # Calculate bucket size
        bucket_range = (maxValue - minValue + 1) / numBuckets

        # Distribute elements into buckets
        for i in range(len(ar)):
            bucket_index = int((ar[i] - minValue) // bucket_range)
            buckets[bucket_index].append(ar[i])

        # Sort each non-empty bucket and merge back to the original list
        j = 0
        for bi in range(numBuckets):
            bucket = buckets[bi]
            if bucket:
                bucket.sort()
                for k in range(len(bucket)):
                    ar[j] = bucket[k]
                    j += 1
                self.notify_array_modified()  # Notify when array is modified

if __name__ == '__main__':
    """
    Example usage
    """
    sorter = BucketSort()

    array = [10, 4, 6, 8, 13, 2, 3]
    sorter.sort(array)
    print(array)

    array = [10, 10, 10, 10, 10]
    sorter.sort(array)
    print(array)
