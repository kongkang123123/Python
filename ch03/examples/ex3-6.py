invite_dinner = []

invite_dinner.append("Wonsik")
invite_dinner.append("Chanhyuk")
invite_dinner.append("Suyeong")
invite_dinner.append("Sangsu")

not_attend = invite_dinner[1]

print(not_attend + " can't come on")

invite_dinner[1] = "Jaechan"

print("I can invite 3 more people.")

invite_dinner.insert(0, "Gibaek")
invite_dinner.insert(2, "Yejun")
# invite_dinner.insert(-1, "Eunseong")    # 마지막 요소에 추가
invite_dinner.append("Eunseong")

print(invite_dinner)