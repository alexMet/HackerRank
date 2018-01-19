import Control.Applicative
import Control.Monad
import System.IO

main = do
   s <- getLine
   putStr . reverse $ foldl (\acc x -> if elem x acc then acc else x : acc) [] s
