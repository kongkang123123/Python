# input() 함수는 매개변수를 하나만 받음 - 사용자가 직접 입력하도록 기다리는 프롬프트에 입력한 값.
message = input("Tell me something and I will repeat it back to you: ")
print(message)

# 한 행을 넘는 프롬프트가 필요할 때는 프롬프트를 변수에 저장하고 그 변수를 input() 함수에 넘김
prompt = "If you tell us who you are we can personalize the messages you see."
prompt += "\nWhat is your first neme? "

name = input(prompt)
print("\nHello " + name + "!")

### 사용자가 멈출 수 있도록 만들기 ###
prompt = "\n Tell me something and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""

active = True

while(message != 'quit'):
    message = input(prompt)
    if(message != 'quit'):
        print(message)

### 플래그 사용하기 ###
# flag: 전체 프로그램을 계속할지 끝낼지를 판단하느 변수
active = True

while(active):
    message = input(prompt)

    if(message == 'quit'):
        active = False
    else:
        print(message)