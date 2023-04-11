addFunction arg1 arg2 = arg1 + arg2
five = addFunction 3 2

exclaim sentence = sentence ++ "!"
s = exclaim "Hello"

double::Int->Int
double x = x*2

-- Currying example

average::Float -> Float -> Float -> Float

average a b c = (a+b+c) /3.0
-- result = average 3.0
-- result 4.0 

-- bar:: Num a => a -> a -> a -> a
-- bar x y = x * y 

foo:: (Num a, Show a) => a -> a  -> String
foo x y = show (x * y) 

swap::(Integer, String) -> (String, Integer)
swap (x,y) = (y,x)

mult x y = x * y 

-- getting the value 3 from first tuple
courses = [("cs355",3), ("cs360",2), ("cs350",4)]
-- ((course,grade):xs) = courses
((_,grade):_) = courses

factorial n = if n > 1
              then n * factorial (n-1) -- recursion case
              else 1 -- base case

-- add first n natural numbers
natSum n | n == 0 = 0
         | n > 0 = n + natSum (n-1)
         | otherwise = error "natSum: input is negative!"

natSum1 0 = 0
natSum1 n | n > 0 = n + natSum (n-1)
         | otherwise = error "natSum: input value is negative!"

natSum2 n = if n > 0
           then n + natSum (n-1)
           else error "natSum: input value is negative!"


-- length of a list
lengthList [] = 0
lengthList (x:xs) = 1 + (length xs)

-- last element of a list
lastElement [] = error "lastElement: no list input at end"
lastElement [x] = x
lastElement (x:xs) = last xs

-- return nth element of a list
nElement [] n = error "nElement: list is empty"
nElement (x:xs) 1 = x
mElement (x:xs) n = (nElement xs (n-1))

-- nthElement guard notation
nElement1 (x:xs) n | (n==1) = x
                   | otherwise = nElement1 xs (n-1)

-- copylist
copylist [] = []
copylist (x:xs) = x : (copylist xs)

-- doublelist
doublelist [] = []
doblelist (x:xs) = (x*2) : (doublelist xs)

-- squarelist
squarelist [] = []
squarelist (x:xs) = (x*x) : (squarelist xs)

-- multiply by value input
multiplymembers [] v = []
multiplymembers (x:xs) v = (v*x) : (multiplymembers xs v)

-- length of sublist
lengthSubList [] = []
lengthSubList (x:xs) = (length x) : (lengthSubList xs)

-- check odd
odds [] = []
odds (x:xs) | ((x `mod` 2) == 1) = x : (odds xs)
            | otherwise = odds xs

-- filterSmaller 
filterSmaller [] v = []
filterSmaller (x:xs) v | (x >= v) = x : (filterSmaller xs v)
                       | otherwise = filterSmaller xs v

addup :: Num p => [p] -> p
addup [] = 0
addup (x:xs) = x + (addup xs)

sum1 = addup [1,2,3,4,5]
sum2 = addup [1.0,2.0,3.0,4.0,5.0]

l1 = numbers2sum [1,2,3,4,5,6,7] 15
l2 = numbers2sum [1,2,3,4,5,6,7] 14
l3 = numbers2sum [1,2,3,4,5,6,7] 7


myelem [] ys = []
myelem (x:xs) ys| (x `elem` ys) = x:(myelem xs ys)
                | otherwise = myelem xs ys

longest_list [] = error "List is empty"
longest_list [x] = x
longest_list (x:xs) = x `longer` (longest_list xs)
    where 
        longer list1 list2 | (length list1) >= (length list2) = list1
                           | otherwise = list2

-- rest [] = 0
-- rest (x:xs) = xs

-- HW HINTS
-- 1. merge and sort, use include patterns (x:xs) (y:ys) comparison
-- 2. write a helper function 
-- 3. 

-- Tail Recursive - 1 Stack Frame
addup2::Num p => p -> [p] -> p
addup2 accum [] = accum
addup2 accum (x:xs) = (addup2 (accum +x) xs)

-- Tail Recursive - 1 Stack Frame - More efficient

snoc x xs = xs ++ [x]
reverse' :: [a] -> [a]
reverse' [] = []
reverse' (x:xs) = x `snoc` (reverse' xs)

-- revAppend [1,2,3] [] = [3,2,1] - recursive call is at the end
revAppend [] acc = acc
revAppend (x:xs) acc = revAppend xs (x:acc) 

-- Tail recursive, put everything in bucket -> place bucket to original list

numbers2sum [] n = []
numbers2sum (x:xs) n | ((n-x)<0) = []
                     | otherwise = x: (numbers2sum xs (n-x))

tail_numbers2sum xs n = reverse (tail_helper xs n [])
    where
        tail_helper [] n acc = acc
        tail_helper (x:xs) n acc | (n-x) < 0 = acc
                                | otherwise = (tail_helper xs (n-x) (x:acc) )         

-- Higher order function
-- 1. Takes another function as an argument
-- 2. Returns function as result