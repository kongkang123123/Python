### 함수에서 리스트 수정하기 ###
# 리스트를 함수에 전달하면 그 함수는 리스트를 수정 가능
# 함수 바디에서 리스트에 가한 변경은 영구적이므로
# 데이터양이 많더라도 효율적으로 작동 가능

# 업그레이드 전
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while(unprinted_designs):
    current_design = unprinted_designs.pop()

    print("Printing model: " + current_design)
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


# 변경 후
def print_models(unprinted_designs, completed_models):
    """
    남은 것이 없을 때까지 각 디자인의 출력을 시뮬레이트
    출력한 각 디자인을 completed_models로 옮김
    """
    while(unprinted_designs):
        current_design = unprinted_designs.pop()
        print("Printing model" + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """출력이 끝난 모델 모두 표시"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)