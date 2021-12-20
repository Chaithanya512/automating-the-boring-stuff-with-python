1. re.compile
2. raw strings often used when creating regex objects beacuse they contain escape characters
3. Match obejcts 
4. using group() method
5. group 0 : '(\d\d\d)-(\d\d\d-\d\d\d\d)' <br/>
   group 1 : '(\d\d\d)' <br/>
   group 2 : '(\d\d\d\d)'
6. using backslash, ```\( \)``` 
7. If regex has no groups, it returns list of strings and it returns tuples of strings when regex has groups.
8. | implies "or"
9. used to signify non greedy match and also to match either zero or one of the preceding group.
10. +: one or more <br/>
    *: zero or more
11. {3}: matches for 3 times <br/>
    {3,5}: matches between 3 to 5 times.
12. digit, word, space
13. except digit, except word, except space
14. .*: performs a greedy match <br/>
    .*?: performs a non greedy match
15. [a-z0-9]
16. re.IGNORECASE or re.I
17. ```.``` matches everything except newline whereas ```re.DOTALL``` matches everything including newlines.
18. 'X drummers, X pipers, five rings, X hens'
19. re.VERBOSE allows to add spaces and comments.
20. (r'^\d{1,3} (, \d{3})*$')
21. (r'[A-Z][a-z]*\sWatanabe')
22. (r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)
