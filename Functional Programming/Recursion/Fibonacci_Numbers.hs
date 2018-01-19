--Contributed by Ron Watkins
module Main where

fin 1 = 0
fib 2 = 1
fib n = fst (foldr (\acc (a, b) -> (b, a + b)) (0, 1) [2..n])

main = do
    input <- getLine
    print . fib . (read :: String -> Int) $ input

