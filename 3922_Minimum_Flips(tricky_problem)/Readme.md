# Idea:

If len(s) < 3: return 0

Otherwise, only the sequences of the following forms are coherent:

1. all characters == "0"
2. all characters == "1"
3. only one character == "1"
4. only the first and the last character = "1", all others in the middle == "0"