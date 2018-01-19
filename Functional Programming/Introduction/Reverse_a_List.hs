rev l = if null l  then [] else rev (tail l) ++ [head l]


main = do
		inputdata <- getContents
		mapM_ putStrLn $ map show $ rev $ map (read :: String -> Int) $ lines inputdata
