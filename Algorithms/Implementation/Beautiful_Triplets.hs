main = do
    temp <- getLine
    let [n, d] = map read (words temp) :: [Int]
    a_temp <- getLine
    let a = map read (words a_temp) :: [Int]
    let plusd = map (+ d) a
    let minud = map (subtract d) a
    print $ foldl (\acc x -> if elem x plusd && elem x minud then acc + 1 else acc) 0 a
