def cps_to_cst(cps):
  cst = cps * 0.0075
  return cst

def main():
  cps = float(input("Enter the cps value: "))
  cst = cps_to_cst(cps)
  print(f"The cst equivalent of {cps} cps is {cst} cst.")

if __name__ == "__main__":
  main()
