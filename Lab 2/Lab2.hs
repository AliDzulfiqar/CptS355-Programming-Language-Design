-- CptS 355 - Lab 2 (Haskell) - Fall 2022
-- Name: Muhammad Ali Dzulfiqar
-- Student ID: 11694795

module Lab2
     where
-- 1
{- (a) merge2 -}
-- The function merge2 takes two lists, l1 and l2, and returns a merged list where the elements from l1 
-- and l2 appear interchangeably.  The resulting list should include the leftovers from the longer list and it 
-- may include duplicates.  
-- The type of merge2 should be compatible with   merge2 :: [a] -> [a] -> [a]. 
-- Examples: 
-- > merge2 [3,2,1,6,5,4] [1,2,3] 
-- [3,1,2,2,1,3,6,5,4] 
-- > merge2 "Ct 5" "pS35" 
-- "CptS 355" 
-- > merge2 [(1,2),(3,4)] [(5,6),(7,8),(9,10)] 
-- [(1,2),(5,6),(3,4),(7,8),(9,10)] 
-- > merge2 [1,2,3] [] 
-- [1,2,3] 

merge2 :: [a] -> [a] -> [a]
merge2 l1 [] = l1
merge2 [] l2 = l2
merge2 (x:xs) (y:ys) = x:y: (merge2 xs ys)
                         
{- (b) merge2Tail -}
-- Re-write the merge2 function from part (a) as a tail-recursive function.  Name your function 
-- merge2Tail.  
-- The type of merge2Tail should be compatible with   merge2Tail :: [a] -> [a] -> [a]. 
-- You can use reverse or revAppend in your solution. We defined revAppend in class. 


merge2Tail :: [a] -> [a] -> [a]
merge2Tail l1 l2 = merge2TailHelper l1 l2 []
                    where 
                         revAppend [] acc = acc
                         revAppend (x:xs) acc = revAppend xs (x:acc) 

                         merge2TailHelper [] l2 acc = acc `revAppend` l2
                         merge2TailHelper l1 [] acc = acc `revAppend` l1
                         merge2TailHelper (x:xs) (y:ys) acc = merge2TailHelper xs ys (y:x:acc)

{- (c) mergeN -}
-- Using merge2 function defined above and the foldl function, define mergeN which takes a list of 
-- lists and returns a new list containing all the elements in sublists. The sublists should be merged left to 
-- right, i.e., first two lists should be merged first and the merged list should further be merged with the 
-- third list, etc. Provide an answer using foldl; without using explicit recursion. 
-- The type of mergeN should be compatible with :  mergeN:: [[a]] -> [a] 
-- Examples: 
-- > mergeN ["ABCDEF","abcd","123456789","+=?$"] 
-- "A+1=a?2$B3b4C5c6D7d8E9F" 
-- > mergeN [[3,4],[-3,-2,-1],[1,2,5,8,9],[10,20,30]] 
-- [3,10,1,20,-3,30,2,4,5,-2,8,-1,9] 
-- > mergeN [[],[],[1,2,3]]
-- [1,2,3] 

mergeN:: [[a]] -> [a]
mergeN [] = []
mergeN list = foldl merge2 [] list

-- 2
{- (a) count -}
-- Define a function count which takes a value and a list as input and it count the number of occurrences 
-- of the value in the input list.  Your function should not need a recursion but should use a higher order 
-- function (map, foldr/foldl, or filter). Your helper functions should not be recursive as well, but 
-- they can use higher order functions. You may use the length function in your implementation. 
 
-- The type of the count function should be compatible with   count :: Eq a => a -> [a] -> Int 
-- Examples:  
-- > count [] [[],[1],[1,2],[]] 
-- 2 
-- > count (-5) [1,2,3,4,5,6,7] 
-- 0 
-- > count 'i' "incomprehensibilities" 
-- 5 

count :: Eq a => a -> [a] -> Int
count v list = length((filter (\x -> x == v) list))

{- (b) histogram  -}
-- The function histogram creates a histogram for a given list. The histogram will be a list of tuples 
-- (pairs) where the first element in each tuple is an item from the input list and the second element is the 
-- number of occurrences of that item in the list.  Your function shouldn’t need a recursion but should use 
-- a higher order function (map, foldr/foldl, or filter). Your helper functions should not be 
-- recursive as well, but they can use higher order functions. You may use the count function you defined 
-- in part (a) and eliminateDuplicates function you defined in HW1. 
 
-- The order of the tuples in the histogram can be arbitrary.  The type of the function should be compatible 
-- with  histogram :: Eq a => [a] -> [(a, Int)] 
-- Examples:  
-- > histogram [[],[1],[1,2],[1],[],[]] 
-- [([1,2],1),([1],2),([],3)] 
-- > histogram "macadamia" 
-- [('c',1),('d',1),('m',2),('i',1),('a',4)] 
-- > histogram (show 122333444455555) 
-- [('1',1),('2',2),('3',3),('4',4),('5',5)] 

histogram :: Eq a => [a] -> [(a, Int)]
histogram list = map (\x -> (x, count x list)) (eliminateDuplicates list)
                  where
                    eliminateDuplicates [] = [] 
                    eliminateDuplicates (x:xs) | x `elem` xs = eliminateDuplicates xs
                                               | otherwise = x : eliminateDuplicates xs



-- 3                
{- (a) concatAll -}
-- Function concatAll is given a nested list of strings and it returns the concatenation of all 
-- strings in all sublists of the input list. Your function should not need a recursion but should use functions 
-- “map” and “foldr”. You may define additional helper functions which are not recursive. 
-- The type of the concatAll function should be:  
-- concatAll ::  [[String]] -> String 
 
-- Examples:  
-- > concatAll [["enrolled"," ","in"," "],["CptS","-","355"],[" ","and"," "],["CptS","-","322"]] 
-- "enrolled in CptS-355 and CptS-322" 
-- > concatAll [[],[]]    
-- "" 

concatAll ::  [[String]] -> String 
concatAll string = concatAllHelper (map concatAllHelper string)
                    where concatAllHelper string = foldr (++) [] string

{- (b) concat2Either -}               
data AnEither  = AString String | AnInt Int
                deriving (Show, Read, Eq)

-- Define a Haskell function concat2Either that takes a nested list of AnEither values and it returns 
-- an AString, which is the concatenation of all values  in all sublists of the input list. The parameter of 
-- the AnInt values should be converted to string and included in the concatenated string. You may use 
-- the show function to convert an integer value to a string.  
 
-- Your concat2Either function shouldn’t need a recursion but should use functions “map” and 
-- “foldr”. You may define additional helper functions which are not recursive.  The type of the 
-- concat2Either function should be:   
-- concat2Either:: [[AnEither]] -> AnEither 
 
-- (Note: To implement concat2Either, change your concatAll function and your helper function in 
-- order to handle AnEither values instead of strings.) 
 
-- Examples:  
-- > concat2Either [[AString "enrolled", AString " ", AString "in", AString " "],[AString "CptS", AString "-", AnInt 355], [AString " ", AString "and", AString " "], [AString "CptS", AString "-", AnInt 322]] 
-- AString "enrolled in CptS-355 and CptS-322" 
-- > concat2Either [[AString "", AnInt 0],[]] 
-- AString "0" 
-- > concat2Either [] 
-- AString ""  
 
-- concatMaybe -- similar problem as concat2Either

-- -- 1. Write helper 'maybe_concat' to concat two maybe values
-- maybe_concat (Nothing) (Nothing) = Nothing
-- maybe_concat (Just x) (Nothing) = Just x
-- maybe_concat (Nothing) (Just y) = Just y
-- maybe_concat (Just x) (Just y) = Just (x ++ y)

-- -- 2. maybe_concat to implement concat_maybelist
-- concat_maybelist xs = foldl maybe_concat (Just "") xs

-- -- 3. use map, 'maybe_concat', 'concat_maybelist' to implement concatMaybe
-- concatMaybe list = concat_maybelist (map concat_maybelist list)

concat2Either:: [[AnEither]] -> AnEither 
concat2Either list = concatList (map concatList list)
                      where
                         eitherConcat (AString x) (AString y) = AString (x ++ y)
                         eitherConcat (AString x) (AnInt y) = AString (x ++ show y)
                         eitherConcat (AnInt x) (AString y) = AString (show x ++ y)
                         eitherConcat (AnInt x) (AnInt y) = AString (show x ++ show y)

                         concatList xs = foldl eitherConcat (AString "") xs

-- -- 4      
-- {-  concat2Str -}
-- Re-define your concat2Either function so that it returns a concatenated string value instead of an 
-- AString value. Similar to concat2Either, the parameter of the AnInt values should be converted 
-- to string and included in the concatenated string.  
 
-- Your concat2Str function shouldn’t need a recursion but should use functions “map” and 
-- “foldr”. You may define additional helper functions which are not recursive.  The type of the 
-- concat2Str function should be:   
-- concat2Str:: [[AnEither]] -> String 
 
-- (Note: To implement concat2Str, change your concat2Either function and your helper function 
-- in order to return a string value instead of an AnEither value.) 
 
-- > concat2Str [[AString "enrolled", AString " ", AString "in", AString " "],[AString "CptS", AString "-", AnInt 355], [AString " ", AString "and", AString " "], [AString "CptS", AString "-", AnInt 322]] 
-- "enrolled in CptS-355 and CptS-322" 
-- > concat2Str [[AString "", AnInt 0],[]] 
-- "0" 
-- > concat2Str [] 
-- ""  



-- concat2Str:: [[AnEither]] -> String 
concat2Str list = foldr (++) "" (map concatList2Str list)
               where
                    eitherConcat2Str (AString x) y = x ++ y
                    eitherConcat2Str (AnInt x) y = show x ++ y

                    concatList2Str xs = foldr eitherConcat2Str "" xs

                         

                         

data Op = Add | Sub | Mul | Pow
          deriving (Show, Read, Eq)
evaluate:: Op -> Int -> Int -> Int
evaluate Add x y =  x+y
evaluate Sub   x y =  x-y
evaluate Mul x y =  x*y
evaluate Pow x y = x^y
data ExprTree a = ELEAF a | ENODE Op (ExprTree a) (ExprTree a)
                  deriving (Show, Read, Eq)
-- -- 5 
-- {- evaluateTree -}
-- -- 6
-- {- printInfix -}
-- --7
-- {- createRTree -}
data ResultTree a  = RLEAF a | RNODE a (ResultTree a) (ResultTree a)
                     deriving (Show, Read, Eq)
