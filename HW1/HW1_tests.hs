module HW1Tests
    where
import Test.HUnit
import Data.Char
import Data.List (sort)
import HW1
-- P1. merge_sorted tests
p1_test1 = TestCase (assertEqual "merge_sorted-test1" 
                                 [4,5,6]
                                 (merge_sorted [] [4,5,6]) )
p1_test2 = TestCase (assertEqual "merge_sorted-test2" 
                                 "abcdefghijk"
                                 (merge_sorted "acdef" "bghijk") ) 

-- P2. sum_range tests
p2_test1 = TestCase (assertEqual "sum_range-test1" 
                                  3
                                  (sum_range (1,2) [0,1,2,3,4,5,6,7,8,9]) ) 
p2_test2 = TestCase (assertEqual "sum_range-test2" 
                                  1
                                  (sum_range (0,1) [0,1,2,3,4,5,6,7,8,9])) 

-- P3. (a) calc_collatz_seq and (b) longest_collatz_seq tests              
p3a_test1 = TestCase (assertEqual "calc_collatz_seq-test1" 
                                  [5,16,8,4,2,1]
                                  (calc_collatz_seq 5) ) 
p3a_test2 = TestCase (assertEqual "calc_collatz_seq-test2" 
                                  [2,1] 
                                  (calc_collatz_seq 2) ) 

p3b_test1 = TestCase (assertEqual "longest_collatz_seq-test1" 
                                  [2,1] 
                                  (longest_collatz_seq 2) ) 
p3b_test2 = TestCase (assertEqual "longest_collatz_seq-test2" 
                                  [3,10,5,16,8,4,2,1]
                                  ((longest_collatz_seq 3)))

-- P4. (a) game_scores and (b) wins_by_year tests  (one test is sufficient for wins_by_year)                                
p4a_test1 = TestCase (assertEqual "game_scores-test1" 
                                  (sort [(20,33),(21,6)])  
                                  (sort $ game_scores wsu_games "CAL") ) 
p4a_test2 = TestCase (assertEqual "game_scores-test2" 
                                  (sort [(21,31)]) 
                                  (sort $ game_scores wsu_games "AFA") )     

p4b_test1 = TestCase (assertEqual "wins_by_year-test1" 
                                  (sort []) 
                                  (sort $ wins_by_year []) )                                                     
-- P5. compress_str tests

p5_test1 = TestCase (assertEqual "(compress_str-test1)" 
                                  "a3" 
                                  (compress_str "aaaa") ) 
p5_test2 = TestCase (assertEqual "(compress_str-test2)" 
                                  "b3"
                                  (compress_str "bbbb") )

-- add the test cases you created to the below list. 
tests = TestList [ TestLabel "Problem 1- test1 " p1_test1,
                   TestLabel "Problem 1- test2 " p1_test2,  
                   TestLabel "Problem 2- test1 " p2_test1,
                   TestLabel "Problem 2- test2 " p2_test2,
                   TestLabel "Problem 3a- test1 " p3a_test1, 
                   TestLabel "Problem 3a- test1 " p3a_test1, 
                   TestLabel "Problem 3b- test1 " p3b_test1, 
                   TestLabel "Problem 3b- test1 " p3b_test2, 
                   TestLabel "Problem 4a- test1 " p4a_test1, 
                   TestLabel "Problem 4a- test2 " p4a_test2, 
                   TestLabel "Problem 4b- test1 " p4b_test1, 
                   TestLabel "Problem 5- test1 " p5_test1,
                   TestLabel "Problem 5- test2 " p5_test2 
                 ] 
                  
-- shortcut to run the tests
run = runTestTT  tests