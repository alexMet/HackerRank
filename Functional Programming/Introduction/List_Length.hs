len :: [a] -> Int
len lst = if null lst then 0 else 1 + len (tail lst)

main = do
		inputdata <- getContents
		putStrLn $ show $ len $ map (read :: String -> Int) $ lines inputdata
