import Control.Applicative
import Control.Monad
import System.IO

calculation 0 _ = putStrLn "1"
calculation r n = do
    let r_temp = n - r
    let n_fact = product [1..n]
    let r_fact = product [1..r_temp]
    let n_r_fact = if n - r_temp == 0 then 1 else product [1..(n - r_temp)]
    putStr . show $ n_fact `div` (r_fact * n_r_fact)
    putStr " "
    calculation (r - 1) n
    
main = do
   n_temp <- getLine
   let n = read n_temp :: Int
   forM_ [0..(n-1)] $ \i  -> do
       calculation i i
