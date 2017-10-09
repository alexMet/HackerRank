import Control.Applicative
import Control.Monad
import System.IO

same [] [] acc = acc
same [] _  acc = acc
same _  [] acc = acc
same (x:xs) (y:ys) acc = if x == y then same xs ys (acc + 1) else acc

main :: IO ()
main = do
    s <- getLine
    t <- getLine
    k_temp <- getLine
    let k = read k_temp :: Int
    let x = same s t 0
    let y1 = (length s) - x
    let y2 = (length t) - x
    let u1 = mod y2 2
    let u2 = mod k 2
    putStrLn $ if y1 == 0 && y2 /= 0 then if (u1 + u2 == 0 || u1 + u2 == 2) || x + y2 > k then "Yes" else "No"
               else if y1 + y2 <= k then "Yes" else "No"
    

