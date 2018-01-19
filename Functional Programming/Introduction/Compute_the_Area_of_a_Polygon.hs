import Control.Applicative
import Control.Monad
import System.IO
import Text.Printf

getArea [] p = p / 2
getArea ((_, _) : []) p = p / 2
getArea ((a, b) : (c, d) : xs) p = getArea ((c, d) : xs) (a * d - b * c + p)
    
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    points <- forM [1..n] (\a0  -> do
        line <- getLine
        let l = words line
        let one = read (head l) :: Double
        let two = read (last l) :: Double
        return (one, two))
    let p = points ++ [head points]
    printf "%.4f\n" $ getArea p 0
