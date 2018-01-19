main = do
    s_temp <- getLine
    let s = s_temp :: String
    putStrLn . reverse $ foldl (\acc x -> if elem x acc then acc else x : acc) "" s
