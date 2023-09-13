def cps_to_cst(cps):
  cst = cps * 0.0075
  return cst

def cst_to_cps(cst):
  cps = cst / 0.0075
  return cps

def main():
  mode = int(input("Enter the mode (1 for cps to cst, 2 for cst to cps): "))
  if mode == 1:
    cps = float(input("Enter the cps value: "))
    cst = cps_to_cst(cps)
    print(f"The cst equivalent of {cps} cps is {cst} cst.")
  elif mode == 2:
    cst = float(input("Enter the cst value: "))
    cps = cst_to_cps(cst)
    print(f"The cps equivalent of {cst} cst is {cps} cps.")
  else:
    print("Invalid mode.")

if __name__ == "__main__":
  main()
