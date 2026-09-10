from client import MSQueue

def main():
    print("=== Testing Michael-Scott Lock-Free Queue ===")
    q = MSQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    v1 = q.dequeue()
    v2 = q.dequeue()
    v3 = q.dequeue()
    v4 = q.dequeue()
    print(f"Dequeued elements: {v1}, {v2}, {v3}, {v4}")

    assert v1 == 10 and v2 == 20 and v3 == 30 and v4 is None
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
