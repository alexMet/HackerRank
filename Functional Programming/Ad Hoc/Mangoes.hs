import Control.Applicative
import Control.Monad
import Data.List
import System.IO

main = do
    temp <- getLine
    let [n, k] = map read (words temp) :: [Int]
    a_temp <- getLine
    let a = map read (words a_temp) :: [Int]
    h_temp <- getLine
    let h = map read (words h_temp) :: [Int]
    let mazi = sortBy (\(x, y) (z, w) -> if y < w then LT else if y == w then if x < z then LT else GT else GT) (zip a h)
    let (_, _, ans) = foldl (\(asum, hsum, p) (ai, hi) -> if (asum + ai) + p * (hsum + hi) <= k then (asum + ai, hsum + hi, p + 1) 
                                                else (asum, hsum, p)) (0, 0, 0) mazi
    print ans
