from math import gcd

class MyFraction:
    num : 0
    denom: 1

    def __init__(self, n, d):
        self.num = int(n / gcd(abs(n), abs(d)))
        self.denom = int(d / gcd(abs(n), abs(d)))
        if self.denom < 0:
            self.denom = abs(self.denom)
            self.num = -1*self.num
        elif self.denom == 0:
            raise ZeroDivisionError

    def __pos__(self, other):
        return self.num*other.denom + self.denom*other.num, self.denom*other.denom

    def __neg__(self, other):
        return self.num*other.denom - self.denom*other.num, self.denom*other.denom

    def __mul__(self, other):
        return self.num*other.num, self.denom*other.denom

    def __truediv__(self, other):
        return self.num*other.denom, self.denom*other.num
    
    def __gt__(self, other):
        return self.num*other.denom > self.denom*other.num
    
    def __str__(self):
        if type(self) is tuple:
            if self[1] < 0:
                return '%s/%s' %(self[0], -1*self[1])
            else:
                return f"{self.num}/{self.denom}"
        elif self.denom == 1:
            return str(self.num)
        else:
            return f"{self.num}/{self.denom}"

    # def __cmp__(self, arg):
    #     if self > arg:
    #         return -1
    #     elif self == arg:
    #         return 0
    #     else:
    #         return 1
        
    def __nonzero__(self):
        if self != 0:
            return True
        else:
            return False
def main():
    f1 = MyFraction(2, 2)
    f2 = MyFraction(3, 4)
    f3 = MyFraction(9, 8)
    print(f1, f2)
    arr = [f1, f2, f3]
    max_fra = max(arr)
    print(max_fra)
    
if __name__ == '__main__':
    main()