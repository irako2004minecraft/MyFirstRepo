def convert_temperature(temp): #функция перевода градусов 
 if temp.endswith('C'): #если температура указана в цельсиях,
  celsius = float(temp[:-1]) #удаляем последний символ С и извлекаем число
  fahrenheit = celsius * 9/5 + 32 #переводим в фаренгейты
  return f'{fahrenheit}F' #формируем строку с результатом
 elif temp.endswith('F'): #то же самое для температуры в фаренгейтах
  fahrenheit = float(temp[:-1])
  celsius = (fahrenheit - 32) * 5/9
  return f'{celsius}C'
 else: #если некорректные данные, выводим соответствующее сообщение
  return 'Некорректный ввод'

def main(): #основная функция для запроса ввода
 user_input = input('Введите температуру в градусах Цельсия или Фаренгейта ') #запрашиваем ввод у пользователя
 result = convert_temperature(user_input) #вызываем первую функцию
 print (result) #выводим результат

main() #запускаем программу