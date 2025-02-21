### 반환값 ###
def get_formatted_name(first_name, last_name):
    """읽기 쉬운 전체 이름을 반환한다."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

### 매개변수를 옵션으로 만들기 ###
def get_formatted_name(first_name, last_name, middle_name=''):  # 옵션으로 정할 매개변수 ''으로 지정
    """읽기 쉬운 전체 이름을 반환한다."""
    if (middle_name):
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'lee', 'hendrix')
print(musician)

musician = get_formatted_name('jimi', 'hendrix')
print(musician)