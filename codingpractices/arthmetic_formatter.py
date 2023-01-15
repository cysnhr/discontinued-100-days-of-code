# 20230115

def arithmetic_arranger(problems):

    # getting that corner case
    c = 0
    for problem in problems:
      c += 1
      if c > 5:
        return "Error: Too many problems."
        break
    
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

      try:
          num1 = int(problem[0])
          num2 = int(problem[2])
      except ValueError:
          return "Error: Numbers must only contain digits."
          
      op = str(problem[1])
      print(op == "+")
      if op != "+" or op != "-":
        return "Error: Operator must be '+' or '-'."

      form_num1 = (" " * longest - len1) + str(num1)
      form_num2 = op + (" " * longest - len2 - 1) + str(num2)
      dashes = "-" * longest + 2
      res = num1 + num2
      res = str(res)
      res = " " * (longest - len(res)) + res
      arranged_problems = f"{form_num1}\n{form_num2}\n{dashes}\n{res}"
      return arranged_problems

"""
  235
+  52
-----
12345

"""

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
