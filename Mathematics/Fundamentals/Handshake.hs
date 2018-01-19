import Control.Applicative
import Control.Monad
import System.IO


main :: IO ()
main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \a0  -> do
        n_temp <- getLine
        let n = read n_temp :: Int
        print $ n * (n - 1) `div` 2

