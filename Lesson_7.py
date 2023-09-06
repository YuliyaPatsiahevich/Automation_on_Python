def paren_checker (string):
    pars={")":"(","]":"["}
    stack = []
    for s in string:
        if s ==")]":
            stack.append (s)
        elif s =="([":
            if len (stack)>0 and stack [-1] == pars[s]:
                stack.pop ()
            else:
                return False
    return len (stack) == 0