import Control.Applicative
import Control.Monad
import System.IO

main = do
    s <- getLine
    let (a, b, c) = foldl (\(c, l, ls) curL -> if l == curL then (c + 1, l, ls) 
                                       else 
                                           if c == 1 then (1, curL, l : ls)
                                           else (1, curL, (reverse $ show c) ++ (l : ls))) (1, head s, "") (tail s)
    putStr . reverse $ (if a == 1 then "" else (reverse $ show a)) ++ (b : c)
