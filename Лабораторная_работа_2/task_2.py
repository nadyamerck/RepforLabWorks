money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
current_spend = spend
month = 0

money_capital -= (current_spend - salary)
while money_capital >= 0:
    month += 1
    current_spend *= (1 + increase)
    money_capital -= (current_spend - salary)
print("Количество месяцев, которое можно протянуть без долгов:", month)
