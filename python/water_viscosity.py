def water_viscosity(temperature):
  """
  Calculates the viscosity of water at a given temperature.

  Args:
    temperature: The temperature in degrees Celsius.

  Returns:
    The viscosity of water in centipoise and centistoke.
  """

  if temperature < -273.15:
    raise ValueError("The temperature must be greater than or equal to -273.15 degrees Celsius.")

  if temperature <= 100:
    viscosity = 0.890 * (1 - 0.0204 * temperature)
    cst = viscosity * 0.0075
    return viscosity, cst
  else:
    return 0.29, 0

def main():
  temperature = float(input("Enter the temperature of water in degrees Celsius: "))
  viscosity, cst = water_viscosity(temperature)
  print(f"The viscosity of water at {temperature} degrees Celsius is {viscosity} cps and {cst} cst.")

if __name__ == "__main__":
  main()
