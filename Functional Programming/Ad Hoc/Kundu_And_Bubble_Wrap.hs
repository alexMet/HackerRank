import Control.Applicative
import Control.Monad
import System.IO
import Text.Printf
    
readInts :: IO [Double]
readInts = fmap (map read.words) getLine

main = do
    [n, m] <- readInts 
    let bubs = n * m
    printf "%.8f\n" $ bubs * (sum $ map (\x -> 1 / x) [1..bubs])
