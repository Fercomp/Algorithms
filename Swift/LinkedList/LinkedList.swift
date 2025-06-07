// Need to be a class because is a reference type???
class Node {
    var value: Int
    var next: Node?

    init(_ value: Int) {
        self.value = value
    }
}

class LinkedList {
    var head: Node?

    func addNode(_ node: Int) {
        let newNode = Node(node)

        if head == nil {
            head = newNode
            return
        }

        var current = head
        while current?.next != nil {
            current = current?.next
        }
        current?.next = newNode
    }

    func printNodes() {
        var current = head
        while current != nil {
            print("aaa")
            current = current?.next
        }
    }
}

let linkedList = LinkedList()
linkedList.addNode(3)
linkedList.addNode(3)
linkedList.addNode(32)
linkedList.addNode(4)
linkedList.printNodes()