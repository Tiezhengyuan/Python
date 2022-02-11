
class RecursionSequence:

    def acc_add(self, n):
        """
        n+(n-1)+...1
        n>=1
        sum(1)=1, sum(2)=2+ sum(1), sum(n)= n + sum(n-1)
        """
        if n <= 1:
            return n
        else:
            return n + self.acc_add(n-1)

    def acc_add2(self,start, end, step):
        """
        #cumulative plus of arithmetic sequence
        #a0+a1+...+an => an=an-1+i,
        # sum(m)=2, sum(m+1)= m+1 + sum(m), sum(n)= n + sum(n-step)
        """
        if start > end:
            return 0
        elif start == end:
            return start
        else:
            return start + self.acc_add2(start+step, end, step)

    def fib(self, n):
        """
        #fibonacci sequence: 
        #f(2)=2, f(1)=1, fib(3)=f(2)+f(1), 
        # fib(4)=f(3)+f(2), fib(n) = fib(n-1) + fib(n-2), 
        """
        if n < 1:
            return None
        elif n == 1 or n == 2:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)


    def cal_factorial(self, x):
        """
        #factorial: f(x)=x(x-1)(x-2)...1
        #f(1)=1, f(2)=2*f(1), f(n)=n*f(n-1)
        """
        if x < 1:
            return None
        if x == 1:
            return 1
        else:
            return x * self.cal_factorial(x-1)
    

    


