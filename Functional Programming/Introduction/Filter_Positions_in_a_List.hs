f lst = if (length lst == 0) then [] else if (length lst == 1) then [] else [head (tail lst)]++ f (tail (tail lst))

main = do
   inputdata <- getContents
   mapM_ putStrLn $ map show $ f $ map (read :: String -> Int) $ lines inputdata

