-- copylist
copylist [] = []
copylist (x:xs) = x : (copylist xs)

-- squarelist
squarelist [] = []
squarelist (x:xs) = (x*x) : (squarelist xs)

-- implemment own map
map' op [] = []
map' op (x:xs) = (op x) : (map' op xs)

-- squarelist implementation using map
squarelist2 xs = map op xs
    where op x = x*x 

-- squarelist implementation using anonymous function
squarelist3 xs = map (\x -> x * x) xs

-- multiplyAll using map and helper
multiplyAll xs v = map (multiplyBy v) xs
    where multiplyBy x v = x * v

-- multiplyAll using map and anonynymous function
multiplyAll2 xs v = map (\x -> v*x) xs


-- anonymous function
-- \x -> x * x
sq = \x -> x * x
-- (\x -> x * x) 5
snoc = \x xs -> xs ++ [x]

-- filter
filter' op [] = []
filter' op (x:xs) | (op x) = x: (filter' op xs)
                  | otherwise = (filter' op xs)

-- rewrite odds using filter and helper
odds2 xs = filter isOdd xs 
        where isOdd x = (x `mod` 2) == 1

-- rewrite odds using filter and anonymous function
odds3 xs = filter (\x -> x  `mod` 2 == 1) xs

-- filterSmaller
filterSmaller [] v = []
filterSmaller (x:xs) v | x >= v = x:filterSmaller xs v
                       | otherwise = filterSmaller xs v

-- filterSmaller using filter and helper
-- filterSmaller2 v (x:xs) = filter (op v x) xs
--                     where op v x = v >= x

-- filterSmaller using filter and anonymous function
filterSmaller3 xs v1 = filter (\x -> x >= v1) xs

-- foldr - right to left
foldr' op base [] = base
foldr' op base (x:xs) = op x (foldr' op base xs)

addup [] = 0
addup (x:xs) = x + (addup xs)

-- addup using foldr - enclose to make it a prefix
addup2 xs = foldr (+) 0 xs

-- minlist 
minlist1 [] = maxBound
minlist1 (x:xs) = x `min` (minlist1 xs)

-- minlist using foldr
minlist2 xs = foldr min maxBound xs

-- reverse
reverse' [] = []
reverse' (x:xs) = x `snoc` (reverse' xs)
                where snoc x xs = xs ++ [x]

-- reverse using foldr
reverse2 xs = foldr (\x xs -> xs ++ [x]) [] xs

-- check if all element is even
-- allEven [] = True
-- allEven (x:xs) = x `allE` (allEven xs)
--             where allE x b = (even x) && base

-- foldl 
foldl' op acc [] = acc
foldl' op acc (x:xs) = (foldl' op (acc `op` x) xs)

-- tail recursive map
tailmap op xL = reverse (aux_map op xL [])
                where aux_map f [] acc = acc
                      aux_map f (x:xs) acc = aux_map f xs ((f x):acc)
                      
-- tail recursive filter
tailfilter op xs = reverse (helper op xs [])
                where 
                    helper op [] acc = acc
                    helper op (x:xs) acc | (op x) = (helper op xs (x:acc))
                                         | otherwise = (helper op xs acc)

-- implement cons0_all
cons0 xs = 0:xs
cons0_all iL = map cons0 iL

-- implement consX_all
consX x xs = x:xs
consX_all x iL = map (consX x) iL

-- using anonymous function
consX_all2 x iL = map (\xs -> x:xs) iL

--find max value in a nested list of integers
maxLL iL = map maxL iL
        where
            maxL xs = foldr max (minBound::Int) xs

-- examples
-- get_seconds without recursion
-- get_seconds [(1, 'H'),(2, 'A'),(3, 'S'),(4, 'K'),(5, 'E'),(6, 'L'),(7, 'L')]

get_seconds xs = map snd xs
get_seconds2 xs = map (\(a,b) -> b) xs

myCatsLog=[((7,2020),[("Oceanfish",7),("Tuna",1),("Whitefish",3),("Chicken",4),("Beef",2)]), 
 ((8,2020),[("Oceanfish",6),("Tuna",2),("Whitefish",1),("Salmon",3),("Chicken",6)]), 
 ((9,2020),[("Tuna",3),("Whitefish",3),("Salmon",2),("Chicken",5),("Beef",2),("Turkey",1),("Sardines",1)]), 
 ((10,2020),[("Whitefish",5),("Sardines",3),("Chicken",7),("Beef",3)]), 
 ((11,2020),[("Oceanfish",3),("Tuna",2),("Whitefish",2),("Salmon",2),("Chicken",4),("Beef",2),("Turkey",1)]), 
 ((12,2020),[("Tuna",2),("Whitefish",2),("Salmon",2),("Chicken",4),("Beef",2),("Turkey",4),("Sardines",1)]),     
 ((1,2021),[("Chicken",7),("Beef",3),("Turkey",4),("Whitefish",1),("Sardines",2)])  ] 

 -- Target one log
 -- log = [("Oceanfish",7),("Tuna",1),("Whitefish",3),("Chicken",4),("Beef",2)]
 -- returns true if "Oceanfish" is more than n

-- Solution Approach
-- checktuple
-- checktuple 4 "Oceanfish" ("Oceanfish", 7) True
checktuple num flavor (f,v) = (flavor == f) && (v > num)
                       

-- checklog
-- checklog 4 "Oceanfish" [("Oceanfish",7),("Tuna",1),("Whitefish",3),("Chicken",4),("Beef",2)]
checklog num flavor log = (length matching) > 0
    where matching = filter (checktuple num flavor) log

-- using foldr and without using length function
checklog2 num flavor log = foldr (\t base -> (checktuple num flavor t) || base) False log

checklog3 num flavor log = foldr (helper) False log 
    where helper t base = (checktuple num flavor t) || base

-- implement get_months
-- get_months catlog num flavor = filter (helper) catlog
--     where helper (month, log) = checklog num flavor log

get_months catlog num flavor = map (\(a,b)->a) (filter (helper) catlog)
    where 
        checktuple num flavor (f,v) = (flavor == f) && (v > num)
        checklog num flavor log = foldr (\t base -> (checktuple num flavor t)|| base) False log
        helper (month, log) = checklog num flavor log

