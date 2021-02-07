income = int(input("Какая выручка в вашей фирме(в рублях)? "))
outcome = int(input("Какие издержки в вашей фирме(в рублях)? "))
result = income - outcome
rent = (result / income) * 100

if result > 0:
    print(f"Ваша фирма отработала с прибылью: {result} руб.")
    print(f"Рентабельность вашей фирмы: {rent} %.")
    people = int(input("Сколько сотрудников в вашей компании? "))
    result_2 = result / people
    print(f"Прибыль на одного сотрудника составила: {result_2} руб.")
else:
    print(f"Ваша фирма отработала с убытком: {result} руб.")
