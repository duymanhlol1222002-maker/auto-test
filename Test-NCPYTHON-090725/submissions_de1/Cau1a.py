# a)
def camel_case(s):
    parts = s.split()
    return parts[0].lower() + ''.join(w.capitalize() for w in parts[1:])
print(camel_case("hello world python"))
