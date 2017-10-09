fn n = if (n == 0) then [] else [n] ++ fn (n-1)

main = do
    n <- readLn :: IO Int
    print (length(fn(n)))
