# Izvadiet skaitļus no 1 līdz 100, bet katru reizi, 
# kad sasniedzat skaitli, kas dalās ar 3 izvadiet "Fizz",
# un katru reizi, kad sasniedzat skaitli, kas dalās ar 5, izvdiet "Buzz".
# Ja skaitlis dalās gan ar 3, gan ar 5, izvadās "FizzBuzz".

for skaitlis in range(1, 101):
    if skaitlis%3==0 and skaitlis%5==0:
      print("FizzBuzz")
    elif skaitlis%3==0:
      print("Fizz")
    elif skaitlis%5==0:
       print("Buzz")
    else:
       print("skaitlis")
       