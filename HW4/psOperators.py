# Name: Muhammad Ali Dzulfiqar
# Course: CptS355
# Assignment 4 Part 1&2
from psItems import Value, ArrayValue, FunctionValue
class Operators:
    def __init__(self):
        #stack variables
        self.opstack = []  #assuming top of the stack is the end of the list
        self.dictstack = []  #assuming top of the stack is the end of the list
        
        #The builtin operators supported by our interpreter
        self.builtin_operators = {
            # TO-DO in part1
            # include the key value pairs where he keys are the PostScrip opertor names and the values are the function values that implement that operator. 
            # Make sure **not to call the functions** 
            "add" : self.add,
            "sub" : self.sub,
            "mul" : self.mul,
            "mod" : self.mod,
            "eq" : self.eq,
            "lt" : self.lt,
            "gt" : self.gt,
            "length" : self.length,
            "getinterval" : self.getinterval,
            "putinterval" : self.putinterval,
            "aload" : self.aload,
            "astore" : self.astore,
            "pop" : self.pop,
            "stack" : self.stack,
            "dup" : self.dup,
            "copy" : self.copy,
            "count" : self.count,
            "clear" : self.clear,
            "exch" : self.exch,
            "roll" : self.roll,
            "dict" : self.psDict,
            "begin" : self.begin,
            "end" : self.end,
            "def" : self.psDef,
            "if" : self.psIf,
            "ifelse" : self.psIfelse,
            "repeat" : self.repeat,
            "forall" : self.forall
        }
    #-------  Operand Stack Operators --------------
    """
        Helper function. Pops the top value from opstack and returns it.
    """
    def opPop(self):
            return self.opstack.pop()

    """
       Helper function. Pushes the given value to the opstack.
    """
    def opPush(self,value):
        self.opstack.append(value)
        
    #------- Dict Stack Operators --------------
    
    """
       Helper function. Pops the top dictionary from dictstack and returns it.
    """   
    def dictPop(self):
            return self.dictstack.pop()

    """
       Helper function. Pushes the given dictionary onto the dictstack. 
    """   
    def dictPush(self,d):
        self.dictstack.append(d)

    """
       Helper function. Adds name:value pair to the top dictionary in the dictstack.
       (Note: If the dictstack is empty, first adds an empty dictionary to the dictstack then adds the name:value to that. 
    """   
    def define(self,name, value):
        if len(self.dictstack) == 0:
            self.dictPush({})
            self.dictstack[0][name] = value
        else:
            self.dictstack[len(self.dictstack) - 1][name] = value
            


    """
       Helper function. Searches the dictstack for a variable or function and returns its value. 
       (Starts searching at the top of the dictstack; if name is not found returns None and prints an error message.
        Make sure to add '/' to the begining of the name.)
    """
    def lookup(self,name):
        name = '/' + name
        for d in reversed(self.dictstack):
            if name in d:
                return d[name]
        print(f"{name} not found in dictstack")
        return None

    
    #------- Arithmetic Operators --------------
    
    """
       Pops 2 values from opstack; checks if they are numerical (int); adds them; then pushes the result back to opstack. 
    """   
    def add(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1,int) and isinstance(op2,int):
                self.opPush(op1 + op2)
            else:
                print("Error: add - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)             
        else:
            print("Error: add expects 2 operands")
 
    """
       Pop 2 values from opstack; checks if they are numerical (int); subtracts them; and pushes the result back to opstack. 
    """   
    def sub(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1,int) and isinstance(op2,int):
                self.opPush(op2 - op1)
            else:
                print("Error: sub - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)             
        else:
            print("Error: sub expects 2 operands")

    """
        Pops 2 values from opstack; checks if they are numerical (int); multiplies them; and pushes the result back to opstack. 
    """    
    def mul(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if isinstance(op1,int) and isinstance(op2,int):
                self.opPush(op1 * op2)
            else:
                print("Error: mul - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)             
        else:
            print("Error: mul expects 2 operands")

    """
        Pops 2 values from stack; checks if they are int values; calculates the remainder of dividing the bottom value by the top one; 
        pushes the result back to opstack.
    """ 
    def mod(self):
        if len(self.opstack) > 1:
            op1 = self.opPop() 
            op2 = self.opPop() 
            if isinstance(op1,int) and isinstance(op2,int):
                self.opPush(op2 % op1)
            else:
                print("Error: mod - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)             
        else:
            print("Error: mod expects 2 operands")
    #---------- Comparison Operators  -----------------
    """
       Pops the top two values from the opstack; pushes "True" is they are equal, otherwise pushes "False"
    """ 
    def eq(self):
        if len(self.opstack) > 1:
            op1 = self.opPop() 
            op2 = self.opPop() 
            if isinstance(op1,int) and isinstance(op2,int):
                self.opPush(op2 == op1)
            elif isinstance(op1, ArrayValue) and isinstance(op2, ArrayValue):
                self.opPush(op1 is op2)
            else:
                print("Error: eq - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)             
        else:
            print("Error: eq expects 2 operands") 

    """
       Pops the top two values from the opstack; pushes "True" if the bottom value is less than the top value, otherwise pushes "False"
    """ 
    def lt(self):
        if len(self.opstack) > 1:
            op1 = self.opPop() 
            op2 = self.opPop() 
            if isinstance(op1,int) and isinstance(op2,int):
                self.opPush(op2 < op1)
            else:
                print("Error: lt - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)             
        else:
            print("Error: lt expects 2 operands")     
        
    """
       Pops the top two values from the opstack; pushes "True" if the bottom value is greater than the top value, otherwise pushes "False"
    """ 
    def gt(self):
        if len(self.opstack) > 1:
            op1 = self.opPop() 
            op2 = self.opPop() 
            if isinstance(op1,int) and isinstance(op2,int):
                self.opPush(op2 > op1)
            else:
                print("Error: gt - one of the operands is not a number value")
                self.opPush(op2)
                self.opPush(op1)             
        else:
            print("Error: gt expects 2 operands") 

    # ------- Array Operators --------------
    """ 
       Pops an array value from the operand opstack and calculates the length of it. Pushes the length back onto the opstack.
       The `length` method should support ArrayValue values.
    """
    def length(self):
        if len(self.opstack) > 0:
            value = self.opPop()
            if isinstance(value, ArrayValue):
                length = len(value.value)
                self.opPush(length)
            else:
                print("Error: value is not an array type")
        else:
            print("Error: opstack is empty")

    """ 
        Pops the `count` (int), an (zero-based) start `index`, and an array constant (ArrayValue) from the operand stack.  
        Pushes the slice of the array of length `count` starting at `index` onto the opstack.(i.e., from `index` to `index`+`count`) 
        If the end index of the slice goes beyond the array length, will give an error. 
    """
    def getinterval(self):
        if len(self.opstack) > 2:
            count = self.opPop()
            index = self.opPop()
            constant = self.opPop()
            if isinstance(count, int) and isinstance(index, int) and isinstance(constant, ArrayValue):
                if count + index <= len(constant.value):
                    slicedarray = ArrayValue(constant.value[index:index + count])
                    self.opPush(slicedarray)
                else:
                    print("Error: index of the slice goes beyond array length")

            else:
                print("Error: value is not an array type")
        else:
            print("Error: getinterval expects 3 operands")

    """ 
        Pops an array constant (ArrayValue), start `index` (int), and another array constant (ArrayValue) from the operand stack.  
        Replaces the slice in the bottom ArrayValue starting at `index` with the top ArrayValue (the one we popped first). 
        The result is not pushed onto the stack.
        The index is 0-based. If the end index of the slice goes beyond the array length, will give an error. 
    """
    def putinterval(self):
        if len(self.opstack) > 2:
            constant1 = self.opPop()
            index = self.opPop()
            constant2 = self.opPop()
            if isinstance(constant1, ArrayValue) and isinstance(index, int) and isinstance(constant2, ArrayValue):
                if index + len(constant1.value) > len(constant2.value):
                    print("Error: index exceeds length")
                else:
                    constant2.value[index:(index + len(constant1.value))] = constant1.value
            else:
                print("Error: value is not an array type")
        else:
            print("Error: putinterval expects 3 operands")
            

    """ 
        Pops an array constant (ArrayValue) from the operand stack.  
        Pushes all values in the array constant to the opstack in order (the first value in the array should be pushed first). 
        Pushes the orginal array value back on to the stack. 
    """
    def aload(self):
        if len(self.opstack) > 0:
            constant = self.opPop()
            if isinstance(constant, ArrayValue):
                for value in constant.value:
                    self.opPush(value)
                self.opPush(constant)
            else:
                print("Error: value is not an array type")
        else:
            print("Error: opstack is empty")
        
    """ 
        Pops an array constant (ArrayValue) from the operand stack.  
        Pops as many elements as the length of the array from the operand stack and stores them in the array constant. 
        The value which was on the top of the opstack will be the last element in the array. 
        Pushes the array value back onto the operand stack. 
    """
    def astore(self):
        if len(self.opstack) > 0:
            constant = self.opPop()
            if isinstance(constant, ArrayValue):
                temp = []
                for i in constant.value:
                    temp.append(self.opPop())
                constant.value = list(reversed(temp))
                self.opPush(constant)
            else:
                print("Error: value is not an array type")
        else:
            print("Error: opstack is empty")
    #------- Stack Manipulation and Print Operators --------------

    """
       This function implements the Postscript "pop operator". Calls self.opPop() to pop the top value from the opstack and discards the value. 
    """
    def pop (self):
        if len(self.opstack) > 0:
            self.opPop()
        else:
            print("Error: opstack is empty")

    """
       Prints the opstack. The end of the list is the top of the stack. 
    """
    def stack(self):
        if len(self.opstack) > 0:
            stack = reversed(self.opstack)
            for values in stack:
                print(values)

    """
       Copies the top element in opstack.
    """
    def dup(self):
        if len(self.opstack) > 0:
            top = self.opPop()
            self.opPush(top)
            self.opPush(top)
        else:
            print("Error: opstack is empty")

    """
       Pops an integer count from opstack, copies count number of values in the opstack. 
    """
    def copy(self):
        if len(self.opstack) > 0:
            count = self.opPop()
            temp = []
            for i in range(count):
                temp.append(self.opPop())
            for i in reversed(temp):
                self.opPush(i)
            for i in reversed(temp):
                self.opPush(i)
        else:
            print("Error: opstack is empty")


    """
        Counts the number of elements in the opstack and pushes the count onto the top of the opstack.
    """
    def count(self):
        count = len(self.opstack)
        self.opPush(count)

    """
       Clears the opstack.
    """
    def clear(self):
        if len(self.opstack) > 0:
            self.opstack.clear()
        else:
            print("Error: opstack is empty")
        
    """
       swaps the top two elements in opstack
    """
    def exch(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            self.opPush(op1)
            self.opPush(op2)
        else:
            print("Error: exch expects 2 operands")

    """
        Implements roll operator.
        Pops two integer values (m, n) from opstack; 
        Rolls the top m values in opstack n times (if n is positive roll clockwise, otherwise roll counter-clockwise)
    """
    def roll(self):
        if len(self.opstack) > 1:
            n = self.opPop()
            m = self.opPop()
            lst = self.opstack
            if isinstance(n, int) and isinstance(m, int):
                start = len(lst) - m
                helper = lst[start:]
                if n > 0:
                    for i in range(n):
                        helper = helper[-1:] + helper[:-1]
                else:
                    for i in range(n, 0):
                        helper = helper[1:] + helper[:1]
                lst[start:] = helper
        else:
            print("Error: roll expects 2 operands")
       

    """
       Pops an integer from the opstack (size argument) and pushes an  empty dictionary onto the opstack.
    """
    def psDict(self):
        if len(self.opstack) > 0:
            self.opPop()
            self.opPush({})
        else:
            print("Error: opstack is empty")

    """
       Pops the dictionary at the top of the opstack; pushes it to the dictstack.
    """
    def begin(self):
        if len(self.opstack) > 0:
            self.dictPush(self.opPop())
        else:
            print("Error: opstack is empty")

    """
       Removes the top dictionary from dictstack.
    """
    def end(self):
        if len(self.dictstack) > 0:
            self.dictPop()
        else:
            print("Error: dictstack is empty")
        
    """
       Pops a name and a value from opstack, adds the name:value pair to the top dictionary by calling define.  
    """
    def psDef(self):
        if len(self.opstack) > 1:
            value = self.opPop()
            name = self.opPop()
            self.define(name, value)
        else:
            print("Error: psDef expects 2 operands")


    # ------- if/ifelse Operators --------------
    """
       Implements if operator. 
       Pops the `ifbody` and the `condition` from opstack. 
       If the condition is True, evaluates the `ifbody`.  
    """
    def psIf(self):
        # TO-DO in part2
        ifbody = self.opPop()
        condition = self.opPop()
        if condition and isinstance(ifbody, FunctionValue):
            ifbody.apply(self)

    """
       Implements ifelse operator. 
       Pops the `elsebody`, `ifbody`, and the condition from opstack. 
       If the condition is True, evaluate `ifbody`, otherwise evaluate `elsebody`. 
    """
    def psIfelse(self):
        # TO-DO in part2
        elsebody = self.opPop()
        ifbody = self.opPop()
        condition = self.opPop()
        if condition:
            ifbody.apply(self)
        else:
            elsebody.apply(self)


    #------- Loop Operators --------------
    """
       Implements repeat operator.   
       Pops the `loop_body` (FunctionValue) and loop `count` (int) arguments from opstack; 
       Evaluates (applies) the `loopbody` `count` times. 
       Will be completed in part-2. 
    """  
    def repeat(self):
        #TO-DO in part2
        loop_body = self.opPop()
        count = self.opPop()
        if isinstance(loop_body, FunctionValue) and isinstance(count, int):
            for i in range(count):
                loop_body.apply(self)

        
    """
       Implements forall operator.   
       Pops a `codearray` (FunctionValue) and an `array` (ArrayValue) from opstack; 
       Evaluates (applies) the `codearray` on every value in the `array`.  
       Will be completed in part-2. 
    """ 
    def forall(self):
        # TO-DO in part2
        codearray = self.opPop()
        array = self.opPop()
        if isinstance(codearray, FunctionValue) and isinstance(array, ArrayValue):
            for i in array.value:
                self.opPush(i)
                codearray.apply(self)

    #--- used in the setup of unittests 
    def clearBoth(self):
        self.opstack[:] = []
        self.dictstack[:] = []

    def cleanTop(self): 
        if len(self.opstack)>1: 
            if self.opstack[-1] is None: 
                self.opstack.pop() 