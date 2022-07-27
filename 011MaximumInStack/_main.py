from MaxStack import MaxStack

def main():
    s = MaxStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(2)
    s.push(10)
    s.push(5)
    s.push(12)
    print('max', s.max())
    print(s.pop())
    print('max', s.max())
    print(s.pop())
    print('max', s.max())
    print(s.pop())
    print('max', s.max())
    print(s.pop())
    print('max', s.max())
    print(s.pop())
    print('max', s.max())
    print(s.pop())
    print('max', s.max())
    print(s.pop())


if __name__ == "__main__":
    main()
