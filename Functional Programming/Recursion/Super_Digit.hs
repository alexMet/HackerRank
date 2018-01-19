import Control.Applicative
import Control.Monad
import Data.Char
import System.IO

main :: IO ()
main = do
    x_temp <- getLine
    let inp = words x_temp :: [String]
    let dr = foldl (\acc x -> acc + digitToInt x) 0 (inp !! 0)
    let k = read (inp !! 1) :: Int
    let superD = mod dr 9
    if superD == 0 then print 9
    else print $ mod (superD * (mod k 9)) 9
