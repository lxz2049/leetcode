#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>

using namespace std;

const int MAX_HEAP_SIZE = 1 << 14;

class BinaryHeap {
private:
	int* heap;
	int size;
	bool isMaxHeap;
	bool compare(int a, int b) {
		return isMaxHeap ? a > b : a < b;
	}
public:
	BinaryHeap(bool isMax) {
		heap = new int[MAX_HEAP_SIZE+1];
		isMaxHeap = isMax;
		size = 0;
	}
	int Size() {
		return size;
	}
	int Top() {
		return size > 0 ? heap[1] : -1;
	}
	void Push(int e) {
		if (size >= MAX_HEAP_SIZE) {
			printf("heap full!\n");
			return;
		}
		//printf("push %d\n", e);
		// push to the end of heap
		int pos = ++size;
		
		// shift up
		for (; pos > 1 && compare(e, heap[pos/2]); pos = pos/2) {
			//printf("bubbling down %d from %d to %d\n", heap[pos/2], pos/2, pos);
			heap[pos] = heap[pos/2];
		}
		heap[pos] = e;
	}
	int Pop() {
		if (size <= 0) {
			printf("heap empty!\n");
			return -1;
		}

		// replace top element with bottom element
		//printf("pop\n");
		int pos = 1;
		int top = heap[pos];
		heap[pos] = heap[size--];

		// shift down
		int tmp = heap[pos];
		int child;
		for (;2 * pos <= size; pos = child) {
			child = 2 * pos;
			if (child < size && compare(heap[child+1], heap[child]))
				child++;
			if (compare(heap[child], tmp)) {
				//printf("bubbling up %d from %d to %d\n", heap[child], child, pos);
				heap[pos] = heap[child];
			}
			else
				break;
		}
		heap[pos] = tmp;
		return top;
	}
};

class MedianFinder {
private:
	BinaryHeap* minHeap;
	BinaryHeap* maxHeap;
public:
	MedianFinder () {
		maxHeap = new BinaryHeap(true);
		minHeap = new BinaryHeap(false);
	}
    void addNum(int num) {
		if (maxHeap->Size() == 0 || num < maxHeap->Top()) {
			maxHeap->Push(num);
		} else {
			minHeap->Push(num);
		}
    }

    // Returns the median of current data stream
    double findMedian() {
		// rebalance two heaps
		while (maxHeap->Size() > minHeap->Size() + 1) {
			//printf("push maxHeap top into minHeap\n");
			minHeap->Push(maxHeap->Pop());
		}
		while (minHeap->Size() > maxHeap->Size()) {
			//printf("push minHeap top into maxHeap\n");
			maxHeap->Push(minHeap->Pop());
		}
		// median is either minHeap's top or the average of the both heap's top
		if (minHeap->Size() == maxHeap->Size()) {
			return ((double)minHeap->Top() + (double)maxHeap->Top()) / 2;
		}
		return maxHeap->Top();
    }
};

void testHeap() {
	BinaryHeap heap(true);
	heap.Push(1);
	heap.Push(2);
	heap.Push(3);
	heap.Push(4);
	printf("%d\n", heap.Pop());
	printf("%d\n", heap.Pop());
	printf("%d\n", heap.Pop());
	printf("%d\n", heap.Pop());
}

void testMedianFinder() {
	MedianFinder finder;
	finder.addNum(1);
	finder.addNum(2);
	finder.addNum(3);
	printf("%f\n", finder.findMedian());
	finder.addNum(1);
	finder.addNum(2);
	finder.addNum(3);
	printf("%f\n", finder.findMedian());
}

int main() {
	testMedianFinder();
	return 0;
}
