# 리스트에 있는 모든 요소 출력
magicians = ['alice', 'david', 'carolina']

# magician은 임시 변수 아무 이름 쓸 수 있지만 단수로 쓰는게 좋음(naming 규칙)
# magicians 리스트에서 각 이름을 거내 magician 변수에 저장.
for magician in magicians:
    print(magician)     # magician에 저장한 이름을 출력
# for 루프 안에서 들여 쓴 행은 모두 루프 안이라고 간주
# 루프 블록: for 루프부터 루프의 마지막 행까지
# indent: 들여쓰기 or 인덴트

# for cat in cats:
#   print(cat)

print("\n\n")

for magician in magicians:
    print(magician.title() + ", that was a great trick!")   # 변수에 저장됐으므로 이런식으로 활용 가능
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")