# 잃어버린 괄호
# 연산식
text = input().split('-')  # '-' 연산자로 리스트 분리, '+'는 그대로 가져감.
result = 0
print(text)

if '+' in text[0]:
    temp = list(map(int, text[0].split('+')))
    result += sum(temp)  # 첫 식에 '+'가 들어가면, 미리 더해준다.
    for i in range(len(text)-1):
        if '+' in text[i+1]:
            temp = list(map(int, text[i+1].split('+')))
            result -= sum(temp)  # 괄호 친 부분의 합을, 음수 형태로 대입한다.
        else:
            # 그 외의 값들은 + 처리를 해주어서 연산한다.
            text[i] = int(text[i+1])  # 문자열 -> 정수 변환
            result -= text[i]  # 괄호가 안쳐진 부분은 '-' 연산이다

else:
    for i in range(len(text)):
        if '+' in text[i]:
            temp = list(map(int, text[i].split('+')))
            result -= sum(temp)  # 괄호 친 부분의 합을, 음수 형태로 대입한다.

        elif i == 0:
            # 첫번째 값에 '+'가 없으면 결과를 + 처리를 해주어야한다.
            text[i] = int(text[i])  # 문자열 -> 정수 변환
            result += text[i]  # 괄호가 안쳐진 부분은 '-' 연산이다.

        else:
            # 그 외의 값들은 + 처리를 해주어서 연산한다.
            text[i] = int(text[i])  # 문자열 -> 정수 변환
            result -= text[i]  # 괄호가 안쳐진 부분은 '-' 연산이다

print(result)
