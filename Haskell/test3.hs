-- Haskell Data Types
data Days = Sunday | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday
            deriving (Show, Eq, Ord)

-- Pattern Matching
isWeekday :: Days -> Bool
isWeekday Sunday = False
isWeekday Saturday = False
isWeekday _ = True

-- Alternative implementation
isWeekday2::Days -> Bool
isWeekday2 day = not (day `elem` [Saturday, Monday])


-- Parametrized Data Construction
data Money = NONE | COIN Int | BILL Int
            deriving (Eq, Show)

x = (COIN 10)
y = (BILL 20)
z = NONE

amount (NONE) = fromIntegral(0)
amount (COIN x) = fromIntegral(x)/100.0
amount (BILL x) = fromIntegral(x)

addMoney1 :: Fractional a => Money -> Money -> a
addMoney1 x y = (amount x) + (amount y)

addMoney2 :: Money -> Money -> Int
addMoney2 (NONE) (NONE) = 0
addMoney2 (COIN x) (COIN y) = x+y
addMoney2 (BILL x) (BILL y) = (x+y)*100
addMoney2 (NONE) (COIN y) = y
addMoney2 (COIN x) (NONE) = x
addMoney2 (NONE) (BILL y) = y*100
addMoney2 (BILL x) (NONE) = x*100
addMoney2 (COIN x) (BILL y) = x + y*100
addMoney2 (BILL x) (COIN y) = y + x*100

addMoney3 :: Money -> Money -> Money
addMoney3 (NONE) (NONE) = COIN 0
addMoney3 (COIN x) (COIN y) = COIN (x+y)
addMoney3 (BILL x) (BILL y) = (COIN ((x+y)*100))
addMoney3 (NONE) (COIN y) = COIN y
addMoney3 (COIN x) (NONE) = COIN x
addMoney3 (NONE) (BILL y) = (COIN (y*100))
addMoney3 (BILL x) (NONE) = (COIN (x*100))
addMoney3 (COIN x) (BILL y) = (COIN (x + y*100))
addMoney3 (BILL x) (COIN y) = (COIN (y + x*100))

-- add two (Maybe Int) values and have the sum as an Int
add_maybe_1::Maybe Int -> Maybe Int -> Int
add_maybe_1 Nothing Nothing = 0
add_maybe_1 Nothing (Just y) = y
add_maybe_1 (Just x) Nothing = x
add_maybe_1 (Just x) (Just y) = x + y

-- add two (Maybe Int) values and have the sum as a Maybe Int
add_maybe_2::Maybe Int -> Maybe Int -> Maybe Int 
add_maybe_2 Nothing Nothing = Nothing
add_maybe_2 Nothing (Just y) = Just y
add_maybe_2 (Just x) Nothing = Just x
add_maybe_2 (Just x) (Just y) = Just (x + y)
 
-- add an Int and a (Maybe Int) values and have the sum as an Int
add_IntAndMaybe::Int -> Maybe Int -> Int
add_IntAndMaybe x Nothing = x
add_IntAndMaybe x (Just y) = x+y

add_IntAndMaybe2 Nothing x = x
add_IntAndMaybe2 (Just y) x = x+y

maybe_list = [Nothing, Just 5, Just 10, Just 12, Nothing, Just (-1)]

-- sum of list using foldl/foldr and have a total sum as (Maybe Int)
out1 = foldr (add_maybe_2) (Nothing) maybe_list

-- sum of list using foldl/foldr and have a total sum as (Int)
out2 = foldl (add_IntAndMaybe) 0 maybe_list

-- sum of list using foldl/foldr and have a total sum as (Int)
out3 = foldr (add_IntAndMaybe2) 0 maybe_list

-- recursive data types
data MyList a = EMPTY | CONS a (MyList a)
                deriving (Show, Eq)

list1 = 1:2:3:4:[]
-- (x:xs) = list1

mylist1 = CONS 1(CONS 2 (CONS 3 (CONS 4 EMPTY)))
-- (CONS ys) = mylist1

-- implement length
length' [] = 0
length' (x:xs) = 1 + length' xs

mylength' (EMPTY) = 0
mylength'(CONS z zs) = 1 + mylength' zs

-- implement IntTree
data IntTree = Leaf Int | Node (IntTree) (IntTree)
               deriving (Show, Eq)

-- implement polymorphisc tree
data Tree a = LEAF a | NODE (Tree a) (Tree a)
              deriving (Show, Eq)

-- imolement ternary tree
data TriTree a = TLEAF a | TNODE (TriTree a) (TriTree a) (TriTree a)
                 deriving (Show, Eq)

-- implement binary tree


-- example tree


-- count tree leaves
nLeaves::Num p => Tree a -> p
nLeaves (LEAF v) = 1
nLeaves (NODE left right) = (nLeaves left) + (nLeaves right)

-- count tree nodes
nNodes (LEAF v) = 0
nNodes (NODE left right) = 1 + (nNodes left) + (nNodes right)

-- max value in leaves
maxTree (LEAF v) = v
maxTree (NODE left right) = (maxTree left) `max` (maxTree right)

-- copy tree
copyTree (LEAF v) = LEAF v
copyTree (NODE left right) = NODE (copyTree left) (copyTree right)

-- tree map
treeMap op (LEAF v) = LEAF (op v)
treeMap op (NODE left right) = NODE (treeMap op left) (treeMap op right)

-- preOrder traversal
preOrder (LEAF v) = v:[]
preOrder (NODE left right) = (preOrder left) ++ (preOrder right)

-- preOrder2 (LEAF v) = v:[]
-- preOrder2 (NODE v left right) = [v] ++ (preOrder left) ++ (preOrder right)

-- inOrder LEAF v = v:[]
-- inOrder (NODE left right) = (inOrder left) (inOrder right)

-- implement STree, where it stores sum of the leaves value
data STree a = STree a | SNode a (STree a) (STree b)
               deriving (Show, Eq)