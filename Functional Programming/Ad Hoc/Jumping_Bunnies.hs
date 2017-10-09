import Control.Applicative
import Control.Monad
import System.IO
        
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    a_temp <- getLine
    let nums = map read (words a_temp :: [String]) :: [Int]
    print $ foldr lcm (head nums) (tail nums)
