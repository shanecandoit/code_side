
import dukpy
import hashlib


def sha(src: str) -> str:
    return hashlib.sha1(src.encode('utf-8')).hexdigest()


def run(src: str) -> str:
    src = src.strip()
    out = '// '+sha(src) + '\n'
    lines = src.split('\n')
    for line in lines:
        out += '// '+line+'\n'
    result = ''
    e = None
    try:
        # random.seed(0) # not fixed Math.random()
        result = str(dukpy.evaljs(src)).strip()
    except Exception as e:
        # print(e)
        for line in str(e).split('\n'):
            out += '// '+line+'\n'
    out += '// ---\n'
    if len(result):
        out += result+'\n'
    # else:
    #    out += ':('
    out += '// ' + sha(src) + '\n'
    ok = len(result) > 0
    # return out, ok, e
    return out


if __name__ == '__main__':

    r = run('2 + 3')
    print(27, r)

    # how errors look?
    r = run('2 + ')
    print(30, r)
    '''
    30 // 91195eae60d9a0b0415916e4f3163560d1e8fddb
    // 2 +
    // SyntaxError: parse error (line 1)
    // 	src\pyduktape.c:1
    // 	duk_js_compiler.c:3655
    // ---
    
    // 91195eae60d9a0b0415916e4f3163560d1e8fddb
    '''

    src = '''
    a=Math.random();
    a;
    '''
    r = run(src)
    print(50, r)
    '''
    50 // 1eb9e1f4845c3d8e27f0683e78bc9a89b9b72856
    // a=Math.random();
    // a;
    // ---
    0.2035559130166008
    // 1eb9e1f4845c3d8e27f0683e78bc9a89b9b72856
    '''

