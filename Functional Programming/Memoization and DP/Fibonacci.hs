import Control.Applicative
import Control.Monad
import System.IO

fib 0 = 0
fib 1 = 1
fib n = fst (foldr (\acc (a, b) -> (b, a + b)) (0, 1) [1..n]) 

main = do
    input <- getLine
    let t = read input :: Int
    forM_ [1..t] $ \_ -> do
        n_temp <- getLine
        let n = read n_temp :: Int
        let m = 10 ^ 8 + 7
        print $ fib n `mod` m

