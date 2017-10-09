f n arr = if (null arr) then [] else (take n (repeat (head arr))) ++ f n (tail arr)

main = do
   n <- readLn :: IO Int
   inputdata <- getContents
   mapM_ putStrLn $ map show $ f n $ map (read :: String -> Int) $ lines inputdata

