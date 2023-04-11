-- CptS 355 - Lab 1 (Haskell) - Fall 2022
-- Name: Muhammad Ali Dzulfiqar

module Lab1
     where

-- 1.insert 

insert 0 item [] = item : []
insert n item [] = []
insert 0 item (x:xs) = item : (xs)
insert n item (x:xs) = x: (insert (n-1) item xs)


-- 2. insertEvery
insertEvery n item iL = insertHelper n item iL n
                        where
                            insertHelper 0 item [] orgN = item:[]
                            insertHelper n item [] orgN = []
                            insertHelper 0 item (x:xs) orgN = item:(insertHelper orgN item (x:xs) orgN)
                            insertHelper n item (x:xs) orgN = x:(insertHelper (n-1) item xs orgN)

-- 3. getSales
storelog = [("Mon",50),("Fri",20), ("Tue",20),("Fri",10),("Wed",25),("Fri",30)]

getSales day [] = 0
getSales day ((x,y):xs)
          | day == x = y + (getSales day xs)
          | otherwise = getSales day xs
                                                  
-- 4. sumSales
sales = [("Amazon",[("Mon",30),("Wed",100),("Sat",200)]), 
         ("Etsy",[("Mon",50),("Tue",20),("Wed",25),("Fri",30)]), 
         ("Ebay",[("Tue",60),("Wed",100),("Thu",30)]), 
         ("Etsy",[("Tue",100),("Thu",50),("Sat",20),("Tue",10)])] 

sumSales store day [] = 0
sumSales store day ((x,(y,z)):xs)
          | (store == x && day == y) = z + (sumSales store day xs)
          | otherwise = sumSales store day xs
 
-- 5. split



-- 6. nSplit