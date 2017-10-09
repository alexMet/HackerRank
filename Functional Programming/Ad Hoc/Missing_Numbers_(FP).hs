import Data.Vector as V
import Data.List as L
import Control.Applicative
import Control.Monad
import System.IO

main = do
    n_temp <- getLine
    a_temp <- getLine
    let a = L.map (\x -> (10000 + read x, 1)) (words a_temp :: [String]) :: [(Int, Int)]
    m_temp <- getLine
    b_temp <- getLine
    let b = L.map (\x -> (10000 + read x, -1)) (words b_temp :: [String]) :: [(Int, Int)]
    let h = V.replicate 20001 0
    let h2 = V.accum (+) h a
    let h = V.accum (+) h2 b
    --let h1 = L.foldl (\v x -> V.update v (fromList [(10000 + x, (v ! (10000 + x)) + 1)])) h a
    --let h = L.foldl (\v x -> V.update v (fromList [(10000 + x, (v ! (10000 + x)) - 1)])) h1 b
    putStrLn $ V.foldr (\(i, x) acc -> if x < 0 then (show (i - 10000)) L.++ " " L.++ acc else acc) "" (V.indexed h)
