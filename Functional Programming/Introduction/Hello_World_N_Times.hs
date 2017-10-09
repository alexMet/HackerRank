import Text.Printf

hello_worlds :: Int -> IO ()
hello_worlds n = printf (foldl (\acc x -> acc ++ "Hello World\n") "Hello World\n" [2..n])


main = do
   n <- readLn :: IO Int
   hello_worlds n

