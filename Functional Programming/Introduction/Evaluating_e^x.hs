import Control.Applicative
import Control.Monad
import System.IO
import Text.Printf

main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    forM_ [1..n] $ \a0  -> do
        x_temp <- getLine
        let x = read x_temp :: Double
        printf "%.4f\n" (foldl (\acc y -> acc + ((x ** y) / product [1..y])) 1.0 [1..9])

