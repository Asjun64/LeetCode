class Minstack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_1 = None
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_1 == None:
            self.min_1 = x
        elif self.min_1 > x:
            self.min_1 = x


    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop(-1)
        if self.stack == []:
            self.min_1 = None
        elif self.min_1 == x:
            self.min_1 = self.stack[0]
            for i in self.stack:
                if i < self.min_1:
                    self.min_1 = i
        return x

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_1


push    46
push    46
push    47
        top
                pop
        GetM
                pop
        GetM
                pop
push    47
        top-
        getM===
push    -48
        top-
        GetM-
                pop-
        GetM-
