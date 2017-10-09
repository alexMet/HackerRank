import Control.Applicative
import Control.Monad
import System.IO

giaPame []       pr pg py pb r g y b = if r == g && y == b then "True" else "False"
giaPame ('R':xs) pr pg py pb r g y b = if abs(pr + 1 - pg) > 1 then "False" else giaPame xs (pr + 1) pg py pb (r + 1) g y b
giaPame ('G':xs) pr pg py pb r g y b = if abs(pr - pg - 1) > 1 then "False" else giaPame xs pr (pg + 1) py pb r (g + 1) y b
giaPame ('Y':xs) pr pg py pb r g y b = if abs(py + 1 - pb) > 1 then "False" else giaPame xs pr pg (py + 1) pb r g (y + 1) b
giaPame ('B':xs) pr pg py pb r g y b = if abs(py - pb - 1) > 1 then "False" else giaPame xs pr pg py (pb + 1) r g y (b + 1)

main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \_ -> do
        s <- getLine
        putStrLn $ giaPame s 0 0 0 0 0 0 0 0
