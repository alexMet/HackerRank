import Control.Applicative
import Control.Monad
import Data.List
import System.IO

gons [] acc = acc
gons ((x, y) : xs) [] = gons xs [(x, y, 1)]
gons ((x, y) : xs) ((a, b, c) : acc) = if x == a then if y < b then gons xs ((a, y, c + 1) : acc)
                                                      else gons xs ((a, b, c + 1) : acc) 
                                       else gons xs ((x, y, 1) : (a, b, c) : acc)

main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \_ -> do
        num <- getLine
        let [n, k] = map read (words num :: [String]) :: [Int]
        ls_temp <- getLine
        let ls = fst $ foldr (\x (xs, ind) -> ((read x :: Int, ind) : xs, ind - 1)) ([], n - 1) (words ls_temp :: [String])
        let lsSort = sortBy (\(a, _) (c, _) -> if a >= c then GT else LT) ls
        let lsCnt = gons lsSort []
        let ansSort = sortBy (\(_, b, _) (_, d, _) -> if b >= d then GT else LT) lsCnt
        let ansFina = foldr (\(a, _, c) acc -> if c >= k then (show a :: String) ++ " " ++ acc else acc) "" ansSort
        putStrLn $ if ansFina == [] then "-1" else ansFina
