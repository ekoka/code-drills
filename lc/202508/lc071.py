"""
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

    A single period '.' represents the current directory.
    A double period '..' represents the previous/parent directory.
    Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
    Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.

The simplified canonical path should follow these rules:

    The path must start with a single slash '/'.
    Directories within the path must be separated by exactly one slash '/'.
    The path must not end with a slash '/', unless it is the root directory.
    The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.

Return the simplified canonical path.

Constraints:
    1 <= path.length <= 3000
    path consists of English letters, digits, period '.', slash '/' or '_'.
    path is a valid absolute Unix path.
"""

def simplified(path):
    n = len(path)
    if n==1: return path
    tokens = []
    i = 0
    while i < len(path):
        while i < n and path[i]=='/':
            i += 1
        tokens.append('/')

        j = i+1
        while j < n and path[j]!='/':
            j += 1
        tokens.append(path[i:j])
        i = j

    res = ['/']
    for t in tokens:
        if t=='.' or t=="": 
            continue
        if t=='/':
            if res[-1]!='/':
                res.append('/')
            continue
        if t=='..':
            if len(res) < 3:
                res = ['/']
            else:
                res.pop()
                res.pop()
            continue
        res.append(t)
    if res[-1]=='/' and len(res) > 1:
        res.pop()
    return "".join(res)

def simplified(path):
    n = len(path)
    tokens = []
    i = 0
    while i < n:
        if path[i]=='/':
            i += 1
            continue
        j = i+1
        while j < n and path[j]!='/':
            j += 1
        t = path[i:j]
        i = j
        if not t: continue
        if t=='.': continue
        if t=='..':
            if len(tokens) < 2:
                tokens = []
            else:
                tokens.pop()
            continue
        tokens.append(t)
    return "/" + "/".join(tokens)




        

if __name__=='__main__':
    path = "/home/"
    exp = "/home"
    res = simplified(path)
    print(res)
    assert exp==res

    path = "/home//foo/"
    exp = "/home/foo"
    res = simplified(path)
    print(res)
    assert exp==res

    path = "/home/user/Documents/../Pictures"
    exp = "/home/user/Pictures"
    res = simplified(path)
    print(res)
    assert exp==res

    path = "/../"
    exp = "/"
    res = simplified(path)
    print(res)
    assert exp==res

    path = "/.../a/../b/c/../d/./"
    exp = "/.../b/d"
    res = simplified(path)
    print(res)
    assert exp==res
