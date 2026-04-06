def length_converter():
    # 1. Define conversion ratios relative to the Meter (m)
    # These represent the "Powers of 10" mentioned in your Physics textbook.
    units = {
        "km": 1000,  # 10^3 (Kilometer)
        "m": 1,  # SI Base Unit (Meter)
        "dm": 0.1,  # 10^-1 (Decimeter)
        "cm": 0.01,  # 10^-2 (Centimeter)
        "mm": 0.001,  # 10^-3 (Millimeter)
        "um": 0.000001,  # 10^-6 (Micrometer)
        "nm": 0.000000001  # 10^-9 (Nanometer)
    }

    print("--- Welcome to Julian's Physics Unit Converter ---")

    try:
        # 2. Input the numerical value to be converted
        value = float(input("Enter the numerical value: "))

        # 3. Input the source and target units
        from_unit = input("Enter the current unit (e.g., km, m, cm, mm): ").lower()
        to_unit = input("Enter the unit to convert to: ").lower()

        if from_unit in units and to_unit in units:
            # Core Physics Logic:
            # First convert to 'meters', then convert from 'meters' to the target unit.
            # Formula: value * (source_ratio / target_ratio)
            result = value * (units[from_unit] / units[to_unit])

            # Use f-strings for output and handle precision with .10g (Scientific Notation)
            print(f"\n[Physics Result]: {value}{from_unit} = {result:.10g}{to_unit}")
        else:
            print("Error: Unit not found. Please check your spelling!")

    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    length_converter()