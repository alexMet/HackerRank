import Control.Applicative
import Control.Monad
import System.IO

main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0 -> do
        temp <- getLine
        let [n, k] = map read (words temp) :: [Integer]
        let a = foldl (\acc x -> div (acc * (n - x + 1)) x) 1 [1..k]
        print $ mod a 100000007
