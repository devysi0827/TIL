# **우선순위 큐와 힙(Heap)**

### **우선순위 큐란?**

\- 우선순위가 가장 높은 데이터를 꺼내는 자료구조입니다.

\- 일반적으로 우선순위 큐는 힙(Heap)이란 자료구조로 구현됩니다. 힙은 트리구조로 가장 높은 우선순위를 가진 것을 루트노드로 정렬합니다. (주로 최소 힙과 최대 힙으로 구현됩니다.)

\- 가중치가 있는 그래프에서 주로 사용합니다. 대표적으로 다잌스트라 알고리즘이 있으며, 이를 통해서 최단 거리를 구하는 알고리즘을 구할 수 있습니다.

\- 힙의 원소를 추가하거나 제거할 때, 트리를 탐색하므로 일반적으로 O(log n)의 시간 복잡도를 가집니다.



### **Heap vs BST(Binary Search Tree)**

\- 힙과 BST는 모두 트리를 기반으로 하는 자료구조입니다. 하지만, 둘은 정렬 부분에서 큰 차이가 있습니다.

\- 힙의 경우 우선순위를 따지는 이진트리로, 부모 노드가 항상 자식 노드보다 우선순위를 가지기만 하면됩니다. (최소 힙의 경우 자식 노드보다 부모 노드가 항상 작거나 같기만 하면됩니다.) 그래서 아래 사진처럼 완벽히 정렬되지 않은 상태를 가질 수도 있습니다.

![img](https://blog.kakaocdn.net/dn/boR3CO/btsknuAuj3m/8kqesBHtC6ClPau6HKSFK1/img.png)

\- BST는 모든 노드가 완벽히 정렬되어 있습니다. 왼쪽 서브트리의 모든 노드는 현재 노드보다 작고 오른쪽 서브트리의 모든 값은 현재 노드보다 큽니다. 

![img](https://blog.kakaocdn.net/dn/xBEUD/btskhabZ0f2/DnhqU2klvN2qK16DbOHIzK/img.png)

### **힙 정렬 (Heap Sort)** 

\- 힙을 이용한 정렬 방식입니다.힙은 항상 우선순위가 가장 높은 원소를 배출하기에 모든 원소를 힙에 넣고 다시 힙에서 빼면 우선순위에 맞게 정렬되어 있습니다.

\- n 개의 원소를 넣고 빼기 때문에 O(n log n)의 시간 복잡도를 가집니다. 



### **힙 코드 (Min Heap)**

```javascript
function createMinHeap() {
    const heap = [];

    function getLeftChildIndex(parentIndex) {
        return 2 * parentIndex + 1;
    }

    function getRightChildIndex(parentIndex) {
        return 2 * parentIndex + 2;
    }

    function getParentIndex(childIndex) {
        return Math.floor((childIndex - 1) / 2);
    }

    function swap(index1, index2) {
        [heap[index1], heap[index2]] = [heap[index2], heap[index1]];
    }

    function heapifyUp() {
        let index = heap.length - 1;
        while (index > 0) {
            const parentIndex = getParentIndex(index);
            if (heap[parentIndex] > heap[index]) {
                swap(parentIndex, index);
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    function extractMin() {
        if (heap.length === 0) {
            return null;
        }
        const minValue = heap[0];
        heap[0] = heap[heap.length - 1];
        heap.pop();
        heapifyDown();
        return minValue;
    }

    function heapifyDown() {
        let index = 0;
        while (getLeftChildIndex(index) < heap.length) {
            const leftChildIndex = getLeftChildIndex(index);
            const rightChildIndex = getRightChildIndex(index);
            const smallerChildIndex =
                rightChildIndex < heap.length && heap[rightChildIndex] < heap[leftChildIndex]
                    ? rightChildIndex
                    : leftChildIndex;
            if (heap[index] > heap[smallerChildIndex]) {
                swap(index, smallerChildIndex);
                index = smallerChildIndex;
            } else {
                break;
            }
        }
    }

    function insert(value) {
        heap.push(value);
        heapifyUp();
    }

    function peek() {
        return heap[0];
    }

    function size() {
        return heap.length;
    }
    

    return {
        insert,
        extractMin,
        peek,
        size,
    };
}
```

\- 배열을 이용하여 트리구조를 구현했다. 트리구조와 동일하게 자신의 숫자 * 2 , 자신의 숫자 * 2 + 1이 각 자식노드가 되며 이를 getChildIndex와 getParentIndex 에서 확인할 수 있습니다.

\- Heap은 부모-자식 간 비교하면서 순서를 바꿀 수 있기 때문에 그를 위한 swap 함수를 구현합니다.

\- heapiyUp은 원소가 추가되었을 때, 사용하는 함수입니다. 원소가 마지막에 추가되면 이 원소는 아직 우선순위에 따라서 정렬되어 있지 않기 때문에 이를 우선순위에 맞게 정렬하는 함수입니다. while문을 이용하여 부모만을 비교하기 때문에 log n 의 시간복잡도를 가집니다.

\- heapiyDown은 반대로, 우선순위가 가장 높은 원소를 제거할 때 사용합니다. 우선순위가 가장 높은 원소 (0번째 원소)를 바로 제거하면 정렬된 상태가 모두 어긋날 수 있기 때문에 마지막 원소랑 바꾼 후, 마지막 원소를 제거하는 방식을 택합니다. 그 후, 가장 위에 원소를 heaipyUp과 반대로 내리면서 정렬합니다.
\- peek, insert, size, extractMin은 이를 사용하는 함수로 아래와 같이 사용할 수 있습니다.

```javascript
const heap = createMinHeap();
heap.insert(5);
heap.insert(10);
heap.insert(3);
heap.insert(8);
console.log(heap.peek()); // 3
console.log(heap.extractMin()); // 3
console.log(heap.size()); // 3
```





### **사진 출처**

유튜브 : https://www.youtube.com/watch?v=AjFlp951nz0

웹사이트 :https://www.geeksforgeeks.org/binary-search-tree-data-structure/