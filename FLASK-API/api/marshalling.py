import marshal
value = (
    "this is a string",
    [1, 2, 3, 4],
    ("more tuples", 1.0, 2.3, 4.5),
    "this is yet another string"
    )
data=marshal.dumps(value)

script = """
print 'hello'
"""

code = compile(script, "<script>", "exec")
module=marshal.dumps(code)

print type(data), len(data)

print marshal.loads(data)
print marshal.loads(module)
