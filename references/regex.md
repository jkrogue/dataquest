# Regex in Python

* [] = matches any character within the bracket (e.g., [bcr]at matches cat, cat, and rat).  Can do ranges with "-" (e.g., [0-9] matches any integer, [a-z] matches any lowercase character)
* ^ = matches the start of the string (e.g., ^cat matches "Cat is here" but not "This is a cat")
* $ = matches the end of the string (e.g., cat$ matches "That is a cat" but not "Cat is here")
* \ = escapes the following character (e.g., \\[Serious\\] matches [Serious])
* {x} = specifies that the previous thing should occur x number times (e.g., [0-9]{3} matches 123)
