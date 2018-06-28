def Reverseprint(head):
    if head:
        Reverseprint(head.next)
        print(head.data)