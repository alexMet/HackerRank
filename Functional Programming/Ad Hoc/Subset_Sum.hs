import Control.Applicative
import Control.Monad
import Data.List
import System.IO
import Data.Array

accSum [] acc = acc
accSum (x:xs) [] = accSum xs [x]
accSum (x:xs) (a:acc) = accSum xs ((x + a) : a : acc)

binsearch xs value low high
   | high < low       = mid + 2
   | xs ! mid > value  = binsearch xs value low (mid - 1)
   | xs ! mid < value  = binsearch xs value (mid + 1) high
   | otherwise        = mid + 1
   where
   mid = low + (high - low) `div` 2
   
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    a_temp <- getLine
    let a = map read (words a_temp :: [String]) :: [Int]
    let aSum = accSum (reverse (sort a)) []
    let ar = array (0, n - 1) $ snd $ foldl (\(i, acc) x -> (i - 1, ((i, x) : acc))) (n - 1, []) aSum
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \_ -> do
        s_temp <- getLine
        let s = read s_temp :: Int
        let ans = binsearch ar s 0 (n - 1) 
        print $ if ans == (n + 1) then -1 else ans
