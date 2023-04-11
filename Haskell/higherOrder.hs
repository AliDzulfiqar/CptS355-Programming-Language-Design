-- CptS 355 - Sample Functions
module HigherOrder_lecture
     where
import Data.Char
-- ======= Examples of "mapping" functions
--copyList
copyList [] = []
copyList (x:xs) = x: (copyList xs)
-- allSquares
allSquares :: Num a => [a] -> [a]
allSquares [] = []
allSquares (x : xs) = x * x : allSquares xs
-- implement our own map
map' op [] = []
map' op (x : xs) = (op x) : (map' op xs)
----------------------------------------------------
-- rewrite allSquares using map
allSquares2 xs  = map square xs
                 where   
                      square x  =  x*x
-- rewrite allSquares using map and anonymous function
allSquares3 xs  = map (\ x  ->  x*x) xs
---------------------------------------------------
{- multiplyAll [1,2,3,4,5] 10 -> [10,20,30,40,50]-}
multiplyAll [] v = []
multiplyAll (x:xs) v = (v * x) : (multiplyAll xs v)
{- multiplyAll (using map and helper function)-}
op v x = v * x
multiplyAll2 xs v = map (op v) xs
{- rewrite multiplyAll using map and anonymous function -}
multiplyAll3 xs v = map (\x -> v*x) xs
----------------------------------------------------
-- ======= Examples of "filtering" functions
-----------------------------------------------------
-- odds
odds [] = []
odds (x:xs)  | ((x `mod` 2) == 1) = x: (odds xs)
             |  otherwise = (odds xs)
-- implement our own filter
filter' op []  = []
filter' op (x:xs) | (op x) = x: (filter' op xs)
                  |  otherwise = (filter' op xs)
tail_filter op xs = reverse (helper op xs [])
   where 
      helper op [] acc  = acc
      helper op (x:xs) acc | (op x) = (helper op xs (x:acc) )
                        |  otherwise = (helper op xs acc)
----------------------------------------------------
{- rewrite "odds" using filter -}
odds2 xs = filter isOdd xs
          where isOdd x  = (x `mod` 2) == 1
      
{- rewrite "odds" using filter and anonymous function -}
odds3 xs = filter (\x -> (x `mod` 2) == 1) xs
----------------------------------------------------
{- filter if smaller than v 
   filterSmaller [3,5,2,1,7,-10,6,5] 5  -}
filterSmaller [] v = [] 
filterSmaller (x:xs) v | (x >= v) = x:(filterSmaller xs v)
                       | otherwise = (filterSmaller xs v)
{- rewrite filterSmaller using filter -}
filterSmaller2  xs v1 = filter (op v1) xs
  where op v2 x = x >= v2  
{- rewrite filterSmaller using filter  and anonymous function -}
filterSmaller3  xs v1 = filter (\x -> x >= v1) xs
----------------------------------------------------
--extractDigits
extractDigits :: String -> String
extractDigits [] = []
extractDigits (chr:xs) | isDigit chr = chr : extractDigits xs
                         | otherwise = extractDigits xs
-- ======= Examples of "reduction" functions
addup []     = 0
addup (x:xs) = x + (addup xs)
addup2 xs = foldr (+) 0 xs
minList1 []     = maxBound
minList1 (x:xs) = x `min` (minList1 xs)
minList2 xs = foldr min maxBound xs
reverse' [] = []
reverse' (x:xs) = x `snoc` (reverse' xs)
                  where 
                       snoc x xs = xs ++ [x]
reverse2 xs = foldr (\x xs -> xs ++ [x]) [] xs 
{- implement our own foldr -}
foldr' op base []     = base
foldr' op base (x:xs) = x `op` (foldr op base xs)
{- implement our own foldl -}
foldl' op acc []     = acc
foldl' op acc (x:xs) =   foldl' op (acc `op` x) xs
-- foldr (+) 0 [1,2,3] 
-- 1 + (foldr (+) 0 [2,3]) 
-- 1 + 2 + (foldr (+) 0 [3]) 
-- 1 + 2 + 3+ foldr (+) 0 [] 
-- 1+2+3+0
-- 1+2+3
-- 1+5
-- 6
-- (foldl  (+)  0 [1,2,3])
-- (foldl  (+)  1 [2,3])
-- (foldl  (+)  3 [3])
-- (foldl  (+)  6 [])
-- 6
-- foldr (:) [] [1,2,3] 
-- 1 : (foldr (:) [] [2,3]) 
-- 1 : 2 : (foldr (:) [] [3]) 
-- 1 : 2 : 3: (foldr (:) [] []) 
-- 1:2:3:[]
-- 1:2:[3]
-- 1:[2,3]
-- [1,2,3]
-- cons base x = x:base
-- (\base x -> x:base)
-- foldl (cons) [] [1,2,3] 
-- foldl (cons) ([] `cons` 1) [2,3] 
-- foldl (cons) ([1] `cons` 2 ) [3] 
-- foldl (cons) ([2,1] `cons` 3) [] 
-- [3,2,1]
---------------------------------------------------------------
--cons x xs = x:xs
--mystery xL = foldr cons [] xL
copylist xL = foldr (\x base -> x:base) [] xL
copylist2 xL = reverse (foldl (\base x -> x:base) [] xL)
---------------------------------------------------------------
{- implement cons0_all
 cons0_all [[1,2],[3],[4,5],[]]   --  [[0,1,2],[0,3],[0,4,5],[0]] -}
cons0 xs = 0:xs
cons0_all iL = map cons0 iL
---------------------------------------------------------------
{- implement consX_all
   consX_all "0"  [["1"],["2","3"],[]]    --  [["0","1"],["0","2","3"],["0"]]  -}
consX x xs = x:xs  -- i.e., (:)
{-using the consX function above-}
consX_all v iL = map (consX v)  iL
{- using anonymous function -}
consX_all2 v iL = map (\xs -> v:xs)  iL
---------------------------------------------------------------
{-  maxLL function
    maxLL [[6,4,2],[-1,7],[1,3],[]] --  7  -}
maxL xs =  foldr max (minBound::Int) xs
-- [maxL [6,4,2],maxL [-1,7],maxL [1,3]]
{- implement maxLL -}
maxLL iL = map maxL iL
   where 
      maxL xs = foldr max  (minBound::Int) xs
foldr1' op [] = error "Exception"
foldr1' op (x:xs) =  foldr op x xs 
-- ("one", 10)
-- helper =  (\x -> x*x) . snd
