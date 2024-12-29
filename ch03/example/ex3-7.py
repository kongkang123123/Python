invite_dinner = []

invite_dinner.append("Wonsik")
invite_dinner.append("Chanhyuk")
invite_dinner.append("Suyeong")
invite_dinner.append("Sangsu")

not_attend = invite_dinner[1]


invite_dinner[1] = "Jaechan"


invite_dinner.insert(0, "Gibaek")
invite_dinner.insert(2, "Yejun")
# invite_dinner.insert(-1, "Eunseong")    # 마지막 요소에 추가
invite_dinner.append("Eunseong")


print("Sorry, " + invite_dinner.pop())
print("Sorry, " + invite_dinner.pop())
print("Sorry, " + invite_dinner.pop())
print("Sorry, " + invite_dinner.pop())
print("Sorry, " + invite_dinner.pop())

print(invite_dinner)

del invite_dinner[0]
del invite_dinner[0]

print(invite_dinner)