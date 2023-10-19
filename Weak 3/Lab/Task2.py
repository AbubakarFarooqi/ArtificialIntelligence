def balance_brackets_recursive(bracket_seq, balance=0, index=0):
    if index == len(bracket_seq):
        return bracket_seq + ')' * balance
    char = bracket_seq[index]
    if char == '(':
        balance += 1
    elif char == ')':
        if balance == 0:
            bracket_seq = '(' + bracket_seq
            balance += 1
        else:
            balance -= 1
    return balance_brackets_recursive(bracket_seq, balance, index + 1)

print(balance_brackets_recursive("(a+b(c)"))