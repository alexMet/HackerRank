import Control.Applicative
import Control.Monad
import System.IO

main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \_ -> do
        temp <- getLine
        let [a, b] = map read (words temp) :: [Int]
        let minn = min a b
        let maxx = max a b
        let riza = floor (sqrt (fromIntegral minn)) :: Int
        print . length $ foldr (\x acc -> 
            if mod minn x == 0 then
                if mod maxx x == 0 then
                    if (div minn x) /= riza && mod maxx (div minn x) == 0 then x : (div minn x) : acc
                    else x : acc
                else 
                    if (div minn x) /= riza && mod maxx (div minn x) == 0 then (div minn x) : acc
                    else acc
            else acc) [] [1..riza]      
