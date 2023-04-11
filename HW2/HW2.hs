-- CptS 355 - Fall 2022 -- Homework2 - Haskell 
-- Name: Muhammad Ali Dzulfiqar
-- Collaborators:  

module HW2 
    where 
        
{- P1 - insert, insert_tail -} 
-- (a) insert – 3% 
-- Write a function insert that takes an integer n, a value item, and a list iL and inserts the item at 
-- index n in the list iL. n is a 1-based index, i.e., item should be inserted after nth element in the list.  
-- If n is greater than the length of the input list, the item will not be inserted. If n is 0, item will be 
-- inserted to the beginning of the list. (You may assume that n >=0.) 
-- This is the insert function you implemented in Lab1.  
 
-- Examples: 
-- > insert 3 100 [1,2,3,4,5,6,7,8] 
-- [1,2,3,100,4,5,6,7,8] 
 
-- > insert 8 100 [1,2,3,4,5,6,7,8] 
-- [1,2,3,4,5,6,7,8,100] 
 
-- > insert 9 100 [1,2,3,4,5,6,7,8] 
-- [1,2,3,4,5,6,7,8] 
 
-- > insert 3 100 [] 
-- [] 

insert 0 item [] = item : []
insert n item [] = []
insert 0 item list = item:list
insert n item (x:xs) = x: (insert (n-1) item xs)

-- (b) insert_tail –  10% 
-- Re-write the insert function from part (a) as a tail-recursive function.  Name your function 
-- insert_tail.  
 
-- You may use the same test cases provided above to test your function.  

insert_tail n item iL = reverse (insert_tail_helper n item iL [])
                        where 
                            insert_tail_helper 0 item [] acc = item:acc
                            insert_tail_helper n item [] acc = acc
                            insert_tail_helper 0 item list acc = (reverse(list))++(item:acc)
                            insert_tail_helper n item (x:xs) acc = insert_tail_helper (n-1) item xs (x:acc)
 
 
 
------------------------------------------------------ 
{- P2  game_scores and wins_by_year  -} 
-- Assume the “wsu_games” data we used in HW1.  
-- wsu_games = 
--         [ (2019, [("NMSU",(58,7)), ("UNCO",(59,17)), ("HOU",(31,24)), ("UCLA",(63,67)),  
--             ("UTAH",(13,38)), ("ASU",(34,38)), ("COLO",(41,10)), ("ORE",(35,37)),   
--             ("CAL",(20,33)), ("STAN",(49,22)), ("ORST",(54,53)), ("WASH",(13,31)),  
--             ("AFA",(21,31))]), 
--             (2020, [("ORST",(38,28)), ("ORE",(29,43)), ("USC",(13,38)), ("UTAH",(28,45))]), 
--             (2021, [("USU",(23,26)), ("PORT ST.",(44,24)), ("USC",(14,45)), ("UTAH",(13,24)),  
--             ("CAL",(21,6)), ("ORST",(31,24)), ("STAN",(34,31)), ("BYU",(19,21)),  
--             ("ASU",(34,21)), ("ORE",(24,38)), ("ARIZ",(44,18)), ("WASH",(40,13)), ("CMU",(21,24))] ) ] 
 
-- (a)  game_scores – 12% 
-- Rewrite the game_scores function in HW1 using higher order functions (map, foldr/foldl, or 
-- filter) and without using recursion. Your helper functions should not be recursive as well, but they 
-- can use higher order functions. 
-- Remember that game_scores takes the game list (similar to wsu_games above) and an opponent 
-- team name (e.g., “USC” ) as input and returns the list of the game scores that WSU played against the 
-- given opponent team. 
-- Examples: 
-- > game_scores wsu_games "USC" 
-- [(13,38),(14,45)] 
-- > game_scores wsu_games "ORST"  
-- [(54,53),(38,28),(31,24)] 
-- > game_scores wsu_games "YALE" 
-- [ ] 

game_scores log school = map (\(school_name, score)->score) (filter (checktuple school) (foldr (++) [] (map(\(year, scores)->scores) log)))
                        where 
                            checktuple school (name, score) = (school == name)

-- game_scores [] school = []
-- game_scores (x:xs) school = game_scores_helper x school ++ game_scores xs school
--                         where
--                             game_scores_helper (year, []) school_wanted = []
--                             game_scores_helper (year, (school_name, score):ys) school_wanted | (school_wanted == school_name) = score : game_scores_helper (year, ys) school_wanted
--                                                                                              | otherwise = game_scores_helper (year, ys) school_wanted
-- (b)  wins_by_year – 12% 
-- Rewrite the wins_by_year function in HW1 using higher order functions (map, foldr/foldl, or 
-- filter) and without using recursion. Your helper functions should not be recursive as well, but they 
-- can use higher order functions. 
-- Remember that wins_by_year takes the WSU game data as input, and it returns a list of tuples where 
-- each tuple includes the year and the number wins (of WSU team) in that year. 
-- Example: 
-- > wins_by_year wsu_games 
-- [(2019,6),(2020,1),(2021,7)] 

-- true if score is higher than opponent

-- -- 1. filter schools that has less score than wsu
-- l0 = ("NMSU",(58,7))
-- l1 = ("NMSU",(8,9)) 


-- l2 = [("NMSU",(58,7)), ("UNCO",(59,17)), ("HOU",(31,24)), ("UCLA",(63,67)),  
--             ("UTAH",(13,38)), ("ASU",(34,38)), ("COLO",(41,10)), ("ORE",(35,37)),   
--             ("CAL",(20,33)), ("STAN",(49,22)), ("ORST",(54,53)), ("WASH",(13,31)),  
--             ("AFA",(21,31))]

-- -- 2. count the list filtered


-- -- 3. return the result as total count and year
-- l3 = (2019, [("NMSU",(58,7)), ("UNCO",(59,17)), ("HOU",(31,24)), ("UCLA",(63,67)),  
--             ("UTAH",(13,38)), ("ASU",(34,38)), ("COLO",(41,10)), ("ORE",(35,37)),   
--             ("CAL",(20,33)), ("STAN",(49,22)), ("ORST",(54,53)), ("WASH",(13,31)),  
--             ("AFA",(21,31))])


wins_by_year log = map (get_wins) log
                where
                    checktuple (name, score) = (fst(score) > snd(score))
                    checklog log = length (map(\(name, score)->score) (filter (checktuple) log)) 
                    get_wins log = (fst(log), checklog (snd(log)))



-- wins_by_year [] = []
-- wins_by_year ((year, y):xs) = (year, wins_by_year_helper (year, y)) : wins_by_year xs
--                     where 
--                         wins_by_year_helper (year, []) = 0
--                         wins_by_year_helper (year, (school_name, (wsu_score, opp_score)):ys) | wsu_score > opp_score = 1 + wins_by_year_helper (year, ys)
--                                                                                              | otherwise = wins_by_year_helper (year, ys) 
    
------------------------------------------------------ 
{- P3  sum_nested_int, sum_nested_item, and sum_my_nested -} 

-- Consider the following Haskell datatype: 
data NestedList  = Item Int 
                 | Array [Int] 
                 deriving (Show, Read, Eq) 
 
-- Note that, Array’s parameter is an [Int] value.   
 
-- (a)  sum_nested_int - 8% 
-- Function sum_nested_int takes a list of NestedItem values as input and it sums all the parameter 
-- values of Item and Array elements in the input list. It returns the overall sum as an Int value.  
-- Your function shouldn’t need a recursion but should use higher order function(s) map, foldr/foldl, 
-- or filter.You may define additional helper functions which are not recursive. 
-- For example,   
-- sum_nested_int [Item 10, Item 5, Array [7,3,12,11], Item 5, Array [9], Array []] 
-- returns  10 + 5 + 7 + 3 + 12 + 11 + 5 + 9 + 0 = 62 
-- Examples: 
-- > sum_nested_int [Item 10, Item 5, Array [7, 3, 12, 11], Item 5, Array [9], Array []] 
-- 62 
-- > sum_nested_int [Array [-3,-5,-6],Array [10, 11],Item (-5),Array [7],Item 1,Item 0] 
-- 10 
-- > sum_nested_int [ ] 
-- 0 



sum_nested_int list = foldl (add_ItemandArray) 0 list
                    where
                        add_ItemandArray x (Item y) = x + y
                        add_ItemandArray x (Array list) = x + (sum list)

-- (b)  sum_nested_item - 5% 
-- Function sum_nested_item takes a list of NestedList values as input and it sums all the parameter 
-- values in Item and Array elements in the input list. It returns the overall sum as an Item value.  
-- Your function shouldn’t need a recursion but should use higher order function(s) map, foldr/foldl, 
-- or filter. You may define additional helper functions which are not recursive.  Also, your function 
-- should not use sum_nested_int that you defined in part(a). 
-- For example,   
-- sum_nested_item [Item 10, Item 5, Array [7,3,12,11], Item 5, Array [9], Array []] 
-- returns  (Item 62). 
-- Examples: 
-- > sum_nested_item [Item 10, Item 5, Array [7,3,12,11], Item 5, Array [9], Array []] 
-- Item 62 
-- > sum_nested_item [Array [-3,-5,-6],Array [10, 11],Item (-5),Array [7],Item 1,Item 0] 
-- Item 10 
-- > sum_nested_item [ ] 
-- Item 0 



sum_nested_item list = foldl (add_ItemandArray2) (Item 0) list
                    where
                        add_ItemandArray2 (Item x) (Item y) = Item (x + y)
                        add_ItemandArray2 (Item x) (Array list) = Item (x + (sum list))

  
-- (c)  sum_my_nested - 12% 
 
-- Now assume we revise the NestedItem datatype and define the following:  
data MyNested  = MyItem Int 
               | MyArray [MyNested] 
               deriving (Show, Read, Eq) 
 
-- Note that, MyArray’s parameter is a [MyNested] value.   
          
-- Define a Haskell function sum_my_nested that takes a list of MyNested values and it returns the sum of 
-- all parameter values of MyItem and MyArray values. Since the parameter of MyArray is a list of  
-- MyNested values, it should recursively add all parameter values in that list.  The function should return 
-- the overall sum as an Int value.  
-- Your function can be recursive and may use higher order functions.  
 
-- Note: A possible solution will use foldr and a helper function which is mutually recursive with 
-- sum_my_nested, i.e., sum_my_nested calls helper and helper calls sum_my_nested.   
 
-- Examples: 
-- > sum_my_nested [MyItem 10, MyItem 5, MyArray  [MyItem 7, MyArray [MyItem 3, MyItem 12], MyItem 11], MyItem 5, MyArray [MyItem 9], MyArray []] 
-- 62 
-- > sum_my_nested [MyArray [MyItem (-2), MyArray [MyItem 3, MyArray [MyItem 12, MyItem (-5), MyArray [MyItem (-8), MyArray[MyItem 3]], MyArray []], MyItem 11], MyItem 5], MyArray [MyItem 9], MyArray[]] 
-- 28 
-- > sum_my_nested [ ] 
-- 0 

sum_my_nested list = foldl (add_ItemandArray3) (0) list
                    where
                        add_ItemandArray3 x (MyItem y) = x + y
                        add_ItemandArray3 x (MyArray list) = x + (foldl (add_ItemandArray3) (0) list)                     

------------------------------------------------------ 
{- P4  tree_height, create_htree, tree_paths -} 
-- In Haskell, a polymorphic binary tree type with data both at the leaves and interior nodes might be 
-- represented as follows: 
data Tree a = Leaf a | Node a (Tree a) (Tree a) 
              deriving (Show, Read, Eq) 
 
-- Assume we modify the above datatype and have each interior node (i.e., Node value) store the height of 
-- the sub-tree rooted at that node. We call this new datatype HTree, defined as follows: 
data HTree a = HLeaf a | HNode a Int (HTree a) (HTree a) 
              deriving (Show, Read, Eq) 
 
-- The Int value in the HNode is the height of the subtree.  
 
-- (a) tree_height - 8% 
-- Write a function tree_height that takes a tree of type (Tree a) and calculates the height of the tree, 
-- i.e., returns the length of the longest path from root to a Leaf node. 
 
tree_height (Leaf v) = 1
tree_height (Node v t1 t2) = 1 + max (tree_height t1) (tree_height t2)

-- Examples: 
-- > tree_height (Node 'C' (Node 'A' (Leaf 'E') (Node 'K' (Leaf 'B') (Leaf 'E'))) (Node 'O' (Node 'M' (Node 'F' (Leaf 'A') (Leaf 'B')) (Leaf 'E')) (Leaf 'E'))) 
-- 5 
-- > tree_height (Node 3 (Node 10 (Node 1 (Leaf 4) (Leaf 5)) (Leaf 6)) (Node 5 (Leaf 8) (Leaf 4))) 
-- 4


 
 
-- (b) create_htree – 10% 
-- Write a function create_htree that takes a tree of type (Tree a) and converts the input tree to a 
-- HTree. The function should recursively traverse the input tree and create a HLeaf value for each Leaf, 
-- and a HNode value for each Node. It should calculate the height of the subtree rooted at that node and 
-- store that value in the created HNode.   
-- For example:  
   
-- Examples: 

-- t1 = Node 3 (Node 10 (Node 1 (Leaf 4) (Leaf 5)) (Leaf 6))  
--             (Node 5 (Leaf 8) (Leaf 4)) 
 
-- t2 = Node 'C' (Node 'A' (Leaf 'E') (Node 'K' (Leaf 'B') (Leaf 'E')))  
--              (Node 'O' (Node 'M' (Node 'F' (Leaf 'A') (Leaf 'B')) (Leaf 'E')) (Leaf 'E')) 

create_htree (Leaf v) = HLeaf v
create_htree (Node v t1 t2) = HNode v h (create_htree t1) (create_htree t2)
                            where
                                h = 1 + max (tree_height t1) (tree_height t2)
 
-- > create_htree t2 
-- HNode 'C' 5 (HNode 'A' 3 (HLeaf 'E') (HNode 'K' 2 (HLeaf 'B') (HLeaf 'E'))) (HNode 'O' 4 (HNode 'M' 3 (HNode 'F' 2 (HLeaf 'A') (HLeaf 'B')) (HLeaf 'E')) (HLeaf 'E')) 
-- > tree_height t1 
-- HNode 3 4 (HNode 10 3 (HNode 1 2 (HLeaf 4) (HLeaf 5)) (HLeaf 6)) (HNode 5 2 (HLeaf 8) 
-- (HLeaf 4)) 



-- (c) find_paths – 13% 
-- Write a function find_paths that takes a tree `t` of type (HTree a)and a value `v` of type a,  and it 
-- finds all paths from the root to the leaf nodes having the value `v`. find_paths returns a nested list 
-- where each sublist corresponds to a path from root to a (HLeaf v) node.   

-- find_paths for the left tree with target value 'E' will return: 
-- ["CAE","CAKE","COME","COE"]  
 
-- The paths to target leaf nodes are marked using colored lines.  
-- ht1 = HNode 3 4 (HNode 10 3 (HNode 1 2 (HLeaf 4) (HLeaf 5)) (HLeaf 6))  
--                 (HNode 5 2 (HLeaf 8) (HLeaf 4))                                    
-- ht2 = HNode 'C' 5 (HNode 'A' 3 (HLeaf 'E') (HNode 'K' 2 (HLeaf 'B') (HLeaf 'E')))  
--                   (HNode 'O' 4 (HNode 'M' 3 (HNode 'F' 2 (HLeaf 'A') (HLeaf 'B'))  
--                   (HLeaf 'E')) (HLeaf 'E'))  

-- > find_paths ht2 'E' 
-- ["CAE","CAKE","COME","COE"] 
-- > find_paths ht2 'A' 
-- ["COMFA"] 
-- > find_paths ht1 4 
-- [[[3,10,1,4],[3,5,4]] 
find_paths tree target = find_paths_helper tree target []
                        where
                            find_paths_helper (HLeaf v) target buf | (target == v) = [reverse (v : buf) ]
                                         | otherwise = [] 
                            find_paths_helper (HNode v h t1 t2) target buf = (find_paths_helper t1 target (v:buf)) ++ (find_paths_helper t2 target (v:buf))


-- 5. Tree examples  – 4% 
-- Create two trees of type Tree. The height of both trees should be at least 4. Test your functions 
-- tree_height, create_htree with those trees. You can further test your create_htree function 
-- using the HTree values returned from create_htree. 
-- The trees you define should be different than those that are given.  Make sure to change the shape of 
-- the trees; just changing the values will not make your trees different. 

tree_examples1 = Node 'A' (Node 'B' (Node 'C' (Leaf 'D') (Leaf 'E')) (Node 'F' (Leaf 'G') (Leaf 'H'))) (Leaf 'I')
tree_examples2 = Node 1 (Node 2 (Node 25 (Node 15 (Leaf 26) (Leaf 17)) (Node 18 (Leaf 19) (Leaf 0))) (Leaf 12)) (Node 3 (Node 4 (Node 5 (Leaf 6) (Leaf 7)) (Node 8 (Leaf 9) (Leaf 10))) (Leaf 11))

-- > tree_height tree_examples1 
-- 4
-- > tree_height tree_examples2
-- 5

-- > create_htree tree_examples1
-- HNode 'A' 4 (HNode 'B' 3 (HNode 'C' 2 (HLeaf 'D') (HLeaf 'E')) (HNode 'F' 2 (HLeaf 'G') (HLeaf 'H'))) (HLeaf 'I')
-- > create_htree tree_examples2
-- HNode 1 5 (HNode 2 4 (HNode 25 3 (HNode 15 2 (HLeaf 26) (HLeaf 17)) (HNode 18 2 (HLeaf 19) (HLeaf 0))) (HLeaf 12)) (HNode 3 4 (HNode 4 3 (HNode 5 2 (HLeaf 6) (HLeaf 7)) (HNode 8 2 (HLeaf 9) (HLeaf 10))) (HLeaf 11))
