porog = float(input("Порог: "))
n = int(input("Количество записей: "))

errors = 0  
previsheniya = 0
countkor = 0
sumkor = 0.0
maximum = None
for _ in range(n):
    line = input()
  
    if line == "error":
        errors = errors + 1
    else:
        value = float(line)
        countkor+= 1
        sumkor+= value

        if value > porog:
            previsheniya += 1

        if maximum is None or value > maximum:
            maximum = value
if countkor>0:
    avg=sumkor/countkor
else:
    avg=0.0

print(n)
print(errors)
print(previsheniya)
if maximum if not None:
    print(f"{maximum:.1f}")
else:
    print("0.0")
print(f"{avg:.1f}")
