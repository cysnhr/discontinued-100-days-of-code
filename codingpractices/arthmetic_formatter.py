# 20230115-20230116

def arithmetic_arranger(problems, answer=False):

    # getting that corner case
    c = 0
    for problem in problems:
      c += 1
      if c > 5:
        return "Error: Too many problems."
        break

    # initiate stuff
    one = []
    two = []
    d = []
    ans = []
  
    for problem in problems:
      problem = problem.split(" ")
      longest = 0
      len1 = len(problem[0])
      len2 = len(problem[2])
  
      # getting the corner cases
      if len1 > 4 or len2 > 4:
        return "Error: Numbers cannot be more than four digits."
        break
      elif len1 > len2:
        longest = len1
      else:
        longest = len2

      longest += 2
      
      try:
          num1 = int(problem[0])
          num2 = int(problem[2])
      except ValueError:
          return "Error: Numbers must only contain digits."
          
      op = str(problem[1])

      if op == "+":
        res = num1 + num2
      elif op == "-":
        res = num1 - num2
      elif op != "+" and op != "-":
        return "Error: Operator must be '+' or '-'."

      form_num1 = ' ' * (longest - len1) + str(num1)
      form_num2 = str(op) + ' ' + ' ' * (longest - 2 - len2) + str(num2)
      dashes = "-" * (longest)
      res = str(res)
      res = " " * (longest - len(res)) + res

      one.append(form_num1)
      two.append(form_num2)
      d.append(dashes)
      ans.append(res)
    
    one = '    '.join(one)
    two = '    '.join(two)
    d = '    '.join(d)
    ans = '    '.join(ans)
    arranged_problems = f"{one}n\n{two}n\n{d}n\n{ans}"
    return arranged_problems



print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
