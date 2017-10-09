import Control.Applicative
import Control.Monad
import System.IO

transform [] acc = acc
transform (x:y:ys) acc = transform ys (x : y : acc)
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    forM_ [1..n] $ \_ -> do
        s <- getLine
        --print $ foldl (\acc x y -> y ++ x ++ acc) "" s
        putStrLn . reverse $ transform s ""
