# Python iterator

# class method python


class Account(object):
    def __init__(self, account_holder):
        self.set_balance(0)
        self.holder = account_holder
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance: return "Insufficient funds"
        self.balance = self.balance - amount
        return self.balance

    def get_balance(self):
        return self.balance 
    
    def set_balance(self, amount):
        if amount < 0:
            raise ValueError ("Balance cannot be negative")
        else:
            self.balance = amount

    balance = property(get_balance, set_balance)

# python iterator example 1
class Letters(object):
    def __init__(self):
        self.current = 'a'
    
    def __next__(self):
        if self.current > 'd':
            raise StopIteration
        result = self.current
        self.current = chr(ord(result)+1)
        return result
    
    def __iter__(self):
        return self

# example 2
class Evens(object):
    def __init__(self):
        self.current = 2
    
    def __next__(self):
        result = self.current
        self.current += 2
        return result

    def __iter__(self):
        return self

# example 3
class NaturalsUptoN(object):
    def __init__(self, init, N):
        self.current = init
        self.N = N

    def __next__(self):
        if self.current > self.N:
            raise StopIteration
        result = self.current
        self.current += 1
        return result

    def __iter__(self):
        return self

# example 4
class copyIter(object):
    def __init__(self, it):
        pass
        
    def __next__(self):
        pass

    def __iter__(self):
        pass

# example 5 - lab 3
class applyNextN(object):
    def __init__(self, op, n, input):
        self.input = input
        self.op = op
        self.current = self._getNextInput()

    def _getNextInput(self):
        try:
            self.current = self.input.__next__()
        except:
            self.current = None
        return self.current

    def __next__(self):
        localN = self.n
        if self.current is None:
            raise StopIteration
        total = self.current
        self.current = self._getNextInput()
        while(localN > 1):
            if self.current is not None:
                total = self.op(total, self.current)
            else:
                break
            localN -= 1
            self.current = self._getNextInput()
        return total


    def __iter__(self):
        return self