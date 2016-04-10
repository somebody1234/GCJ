import Numeric
import Data.Char

main = do
  putStrLn "Case #1:"
  putStr (unlines [concatMap (replicate 2) (showIntAtBase 2 intToDigit ((x + 64) * 2 + 1) "") ++ " " ++ unwords (map show [3..11]) | x <- [0..49]])
