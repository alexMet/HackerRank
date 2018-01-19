import Control.Applicative
import Control.Monad
import System.IO
import Text.Printf

getMetro a b c d = ((c - a) ** 2 + (d - b) ** 2) ** (0.5)

getPerimeter [] p = p
getPerimeter ((_, _) : []) p = p
getPerimeter ((a, b) : (c, d) : xs) p = getPerimeter ((c, d) : xs) (getMetro a b c d + p)
    
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    points <- forM [1..n] (\a0  -> do
        line <- getLine
        let l = words line
        let one = read (head l) :: Double
        let two = read (last l) :: Double
        return (one, two))
    let p = reverse points
    let (c, d) = head p
    let (a, b) = last p
    let start = getMetro a b c d
    printf "%.4f\n" $ getPerimeter p start
