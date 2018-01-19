import Control.Applicative
import Control.Monad
import System.IO

-- H alliws se O(1) einai 3*1-2 + 3*2-2 + ... + 3*n-2 = 3*(1+2+...+n) - 2*n = 3*(n*(n+1)/2) - 2*n = (n * (3*n - 1)) / 2
-- vlepwTeleies 1 acc = acc + 1
-- vlepwTeleies n acc = vlepwTeleies (n - 1) (acc + n * 3 - 2)

main = do
    t_temp <- getLine
    let t = read t_temp :: Int
    forM_ [1..t] $ \_ -> do
        n_temp <- getLine
        let n = read n_temp :: Int
        -- print $ vlepwTeleies n 0
        print $ div (n * (3 * n - 1)) 2
