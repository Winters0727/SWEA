import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    card = input()
    card_list = [card[idx:idx+3] for idx in range(0,len(card),3)]
    card_type = ['S','D','H','C']
    card_cnt = {key:[] for key in card_type}
    for card in card_list:
        key, value = card[0], card[1:]
        if value in card_cnt[key]:
            answer = "ERROR"
            break
        else:
            card_cnt[key].append(value)
    else:
        answer = [13 - len(card_cnt[key]) for key in card_type]
    if type(answer) == list:
        print(f'#{tc}',*answer)
    else:
        print(f'#{tc}',answer)