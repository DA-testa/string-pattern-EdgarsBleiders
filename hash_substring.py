# python3

def read_input():
    try:
        type = input().rstrip()

        if type == "I":
            pattern = input().rstrip()
            text = input().rstrip()
            return (pattern, text)
        
        if type == "F":
            file = input().rstrip()
            with open (file, 'r') as f:
                pattern = f.readline().rstrip()
                text = f.readline().rstrip()
                return (pattern, text)
    except EOFError:
        return None

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurr = []
    P = len(pattern)
    T = len(text)

    if T<P:
        return []
    
    Q = 256
    B = 13
    pattern_hash = 0
    current_hash = 0
    for i in range(P):
        pattern_hash = (pattern_hash * B + ord(pattern[i])) % Q
        current_hash = (current_hash * B + ord(text[i])) % Q

    for i in range(T - P + 1):
        if pattern_hash == current_hash:
            if pattern == text[i:i+P]:
                occurr.append(i)
        

        if i < T - P:
            current_hash = (B * (current_hash - ord(text[i]) * pow(B, P-1, Q)) + ord(text[i+P])) % Q
            current_hash = (current_hash + Q) % Q

    return occurr


if __name__ == '__main__':
    occurr = get_occurrences(*read_input())
    print_occurrences(occurr)