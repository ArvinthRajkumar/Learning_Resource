import ast, secrets, hmac
print(ast.literal_eval("[1, 2, {'a': 3}]"))
try:
    ast.literal_eval("__import__('os').system('echo hi')")
except ValueError:
    print("refused to evaluate code")
token = secrets.token_hex(8)
print(len(token), hmac.compare_digest("abc", "abc"))
