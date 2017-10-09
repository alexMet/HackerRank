f :: Int -> [Int] -> [Int]
f n arr = if (null arr) then []
          else let h = head arr in if (h < n) then [h] ++ f n (tail arr) else f n (tail arr)

main = do 
    n <- readLn :: IO Int 
    inputdata <- getContents 
    let 
        numbers = map read (lines inputdata) :: [Int] 
    putStrLn . unlines $ (map show . f n) numbers

