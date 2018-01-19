import Control.Applicative
import Control.Monad
import System.IO

rotarianos _ 0 _ = putStrLn ""
rotarianos l n x = do
    putStr . take l $ tail x
    putStr " "
    rotarianos l (n - 1) (tail x)

main = do
   n <- readLn :: IO Int
   forM_ [1..n] $ \a0  -> do
        x <- getLine
        let l = length x
        rotarianos l l $ x ++ x
