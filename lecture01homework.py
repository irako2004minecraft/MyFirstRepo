import math
def thirdside(a, b, ugol_grad):
    v_radian = math.radians(ugol_grad)#переводим величину угла из градусов в радианы
    c_squared = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(v_radian)) #применяем теорему косинусов
    return c_squared
#просим пользователя ввести данные
side_a = float(input("Введите длину одной стороны треугольника: "))
side_b = float(input("Введите длину другой стороны треугольника: "))
ugol_grad = float(input("Введите угол в градусах: "))
third_side_length = thirdside(side_a, side_b, ugol_grad)  #находим третью сторону
print(f"Длина третьей стороны треугольника составляет: {third_side_length:.2f}")  #вывод результата