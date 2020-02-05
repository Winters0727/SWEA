import sys

sys.stdin = open('sample_input.txt')

def ppprint(word):
    length = len(word)
    print('.' + ('.#.' + '.')*length)
    print('.' + '#.'*(length*2))
    print('#.' + '.#.'.join(word) + '.#')
    print('.' + '#.'*(length*2))
    print('.' + ('.#.' + '.')*length)

T = int(input())
for tc in range(1,T+1):
    word = input()
    ppprint(word)