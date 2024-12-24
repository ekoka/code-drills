"""
LC 071: Simplify Path

Given an absolute path for a Unix-style file system, which begins with a slash '/', transform this path into its simplified canonical path.

In Unix-style file system context, a single period '.' signifies the current directory, a double period ".." denotes moving up one directory level, and multiple slashes such as "//" are interpreted as a single slash. In this problem, treat sequences of periods not covered by the previous rules (like "...") as valid names for files or directories.

The simplified canonical path should adhere to the following rules:

    It must start with a single slash '/'.
    Directories within the path should be separated by only one slash '/'.
    It should not end with a slash '/', unless it's the root directory.
    It should exclude any single or double periods used to denote current or parent directories.

Return the new path.

Example 1:

Input: path = "/home/"

Output: "/home"

Explanation:

The trailing slash should be removed.

Example 2:

Input: path = "/home//foo/"

Output: "/home/foo"

Explanation:

Multiple consecutive slashes are replaced by a single one.

Example 3:

Input: path = "/home/user/Documents/../Pictures"

Output: "/home/user/Pictures"

Explanation:

A double period ".." refers to the directory up a level.

Example 4:

Input: path = "/../"

Output: "/"

Explanation:

Going one level up from the root directory is not possible.

Example 5:

Input: path = "/.../a/../b/c/../d/./"

Output: "/.../b/d"

Explanation:

"..." is a valid name for a directory in this problem.

Constraints:

    1 <= path.length <= 3000
    path consists of English letters, digits, period '.', slash '/' or '_'.
    path is a valid absolute Unix path.

"""
def simplepath(path):
    path = list(path)
    path.append("/")
    path_stack = [""]
    token = ""
    for c in path:
        if c=="/":
            if token=="..":
                path_stack.pop()
            elif token!="." nd token!="":
                path_stack.append(token)
            token = ""
        else:
            token += c
    return "/".join(path_stack)

# 18
def canonical_path(path):
    path_list = []
    for token in tokenize(path):
        if token=='..':
            if path_list:
                path_list.pop()
            continue
        if token=='.':
            continue
        path_list.append(token)
    return ''.join(('/', "/".join(path_list)))

def tokenize(path):
    start, stop, tokens = None, None, []
    for i in range(len(path)):
        if path[i]!='/':
            if start is None:
                start, stop = i, i+1
            else:
                stop += 1
        elif start:
            tokens.append(path[start:stop])
            start, stop = None, None
    if start:
        tokens.append(path[start:stop])
    return tokens

path = "/home/"
print(canonical_path(path))
# Output: "/home"

path = "/home//foo/"
print(canonical_path(path))
# Output: "/home/foo"

path = "/home/user/Documents/../Pictures"
print(canonical_path(path))
# Output: "/home/user/Pictures"

path = "/../"
print(canonical_path(path))
# Output: "/"

path = "/.../a/../b/c/../d/./"
print(canonical_path(path))
# Output: "/.../b/d"
