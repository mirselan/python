first = int(input("Сколько км. спортсмен пробежал в 1-й день тренировок? "))
last = int(input("Сколько км. нужно пробежать в последний день тренировок? "))
count = 1

while first < last:
    count += 1
    first = first + (first * 0.1)

print(f"На {count}-й день спортсмен достиг результата — не менее {last} км.")
