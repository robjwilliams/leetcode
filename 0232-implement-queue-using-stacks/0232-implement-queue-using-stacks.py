class MyQueue:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        aux_stack = []

        for i in range(1, len(self.stack)):
            aux_stack.append(self.stack[i])
            
        res = self.stack[0]
        
        self.stack = aux_stack

        return res
        

    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        return not self.stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()