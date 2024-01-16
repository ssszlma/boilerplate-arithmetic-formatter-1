def arithmetic_arranger(problems, solve=False):
  L1 = ""
  L2 = ""
  L3 = ""
  L4 = ""
  
  if(len(problems) >= 6):
    return "Error: Too many problems."

  for problem in problems:
    num1 = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    num2 = problem.split(" ")[2]

    if (len(num1) > 4 or len(num2) > 4):
      return "Error: Numbers cannot be more than four digits."

    if not num1.isdigit() or not num2.isdigit():
      return "Error: Numbers must only contain digits."

    if operator == "+":
      res = int(num1) + int(num2)
    elif operator == "-":
      res = int(num1) - int(num2)
    else: 
      return "Error: Operator must be '+' or '-'."
    ans = str(res)

    alignment = max(len(num1), len(num2))
    width = alignment + 2
    dashes = "-" * width
    spaces = '    '

#        32      3801      45      123
#     + 698    -    2    + 43    +  49
#     -----    ------    ----    -----

    line1 = ""
    line1 = f'{num1.rjust(width)}'
    L1 = L1 + line1 + spaces

    line2 = ""
    line2 = operator + f'{num2.rjust(width-1)}'
    L2 = L2 + line2 + spaces

    line3 = ""
    line3 = f'{dashes.rjust(width-1)}'
    L3 = L3 + line3 + spaces

    line4 = ""
    line4 = f'{ans.rjust(width)}'
    L4 = L4 + line4 + spaces

    if solve:
      arranged_problems = L1 + "\n" + L2 + "\n" + L3 + "\n" + L4
    else:
      arranged_problems = L1 + "\n" + L2 + "\n" + L3

    return arranged_problems

    

    

    