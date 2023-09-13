def cst_to_cps(cst):
  cps = cst / 0.0075
  return cps

def main():
  cst = float(input("Enter the cst value: "))
  cps = cst_to_cps(cst)
  print(f"The cps equivalent of {cst} cst is {cps} cps.")

if __name__ == "__main__":
  main()
