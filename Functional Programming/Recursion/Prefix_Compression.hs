getPrefix [] ys acc = ([], ys, acc)
getPrefix xs [] acc = (xs, [], acc)
getPrefix (x:xs) (y:ys) acc = if x == y then getPrefix xs ys (x:acc) else ((x:xs), (y:ys), acc)

main = do
    a_temp <- getLine
    let a = a_temp :: String
    b_temp <- getLine
    let b = b_temp :: String
    let (rema, remb, pref) = getPrefix a b []
    putStrLn $ (show (length pref)) ++ " " ++ (reverse pref)
    putStrLn $ (show (length rema)) ++ " " ++ rema
    putStrLn $ (show (length remb)) ++ " " ++ remb
