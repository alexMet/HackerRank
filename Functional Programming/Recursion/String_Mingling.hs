import Control.Applicative
import Control.Monad
import System.IO

main = do
   p <- getLine
   q <- getLine
   putStr . reverse . snd $ foldl (\(x : xs, y) z -> (xs, x : z : y)) (q, []) p
