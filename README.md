# String Compression Kata

## Instructions
Given a character sequence, client suggests a string compression function working like this :
```
“aabcccaaa” => “a2b1c3a3”
```

To do:
1. Code this function
2. Suggest improvements
3. Code your improvements

## Suggested improvements
1. Optimize the execution speed using "join" instead of concatenating the string
2. Discards compression when the length of the compressed version is greater than that of the original version, e.g.: "ab" => "a1b1".
3. Handle incompatible input string cases, e.g: "a1b3"
4. Add case sensitive options
