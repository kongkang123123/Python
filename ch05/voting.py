age = 15

if (age >= 18):                                 # 이런식으로 괄호로 conditional_test 삽입 가능
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")   # if문도 마찬가지로 : 들여 쓴 행 모두 실행
else:                                           # if문의 조건식이 False 되면 else 실행 시킴
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")