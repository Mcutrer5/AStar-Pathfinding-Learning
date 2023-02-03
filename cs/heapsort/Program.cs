using System;

namespace heapsort {
    class Heap {
        // Driver code
        public static void Main(String[] args) {
            List<int> hT = new List<int>();
            Heap h = new Heap();
            h.push(hT, new Tuple<int, int>(3, 1));
            h.push(hT, new Tuple<int, int>(4, 1));
            h.push(hT, new Tuple<int, int>(9, 1));
            h.push(hT, new Tuple<int, int>(5, 1));
            h.push(hT, new Tuple<int, int>(2, 1));
            Console.WriteLine("Max-Heap array: ");
            h.printArray(hT, hT.Count);
        }

        void heapify(List<int> hT, int i){
            int size = hT.Count;
            // Find the largest among root, left child and right child
            int largest = i;
            int l = 2*i + 1;
            int r = 2*i + 2;
            if (l < size && hT[l] > hT[largest])
                largest = l;
            if (r < size && hT[r] > hT[largest])
                largest = r;

            // Swap and continue heapifying if root is not largest
            if (largest != i) {
                int swap = hT[i];
                hT[i] = hT[largest];
                hT[largest] = swap;
                heapify(hT, largest);
            }
        }

        // Function to insert an element into the tree
        void insert(List<int> hT, int newNum) {
            int size = hT.Count;
            if (size == 0) {
                hT.Add(newNum);
            } else {
                hT.Add(newNum);
                for (int i = size/2 - 1; i >= 0; i--) {
                    heapify(hT, i);
                }
            }
        }

        // Function same as insert but takes a tuple as input instead of int
        void push(List<int> hT, Tuple<int, int> newNum) {
            int size = hT.Count;
            if (size == 0) {
                hT.Add(newNum.Item1);
            } else {
                hT.Add(newNum.Item1);
                for (int i = size/2 - 1; i >= 0; i--) {
                    heapify(hT, i);
                }
            }
        }

        // Function to delete an element from the tree
        void deleteNode(List<int> hT, int num) {
            int size = hT.Count;
            int i;
            for (i = 0; i < size; i++) {
                if (num == hT[i])
                    break;
            }

            int temp = hT[i];
            hT[i] = hT[size - 1];
            hT[size - 1] = temp;
            hT.RemoveAt(size - 1);
            for (int j = size/2 - 1; j >= 0; j--) {
                heapify(hT, j);
            }
        }

        // Print the tree
        void printArray(List<int> array, int size) {
            for (int i = 0; i < size; ++i)
                Console.Write(array[i] + " ");
            Console.WriteLine();
        }
    }
    
}