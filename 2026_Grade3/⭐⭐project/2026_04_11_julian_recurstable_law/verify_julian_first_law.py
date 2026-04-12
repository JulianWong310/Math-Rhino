def verify_julian_first_law(B, k, n):
    # Calculate the Stable Tail (T)
    T = (B ** 2) % (10 ** k)
    # Calculate the Julian Constant (C)
    C = (B * T - T) // (10 ** k)

    # Starting Leading Part (A_2)
    A = (B ** 2) // (10 ** k)

    for n in range(3, n+1):

        # Applying Julian's First Law: A_n = B * A_{n-1} + C
        predict_A = B* A + C

        # Calculating actual value for validation
        actual_A = (B ** n) // (10 ** k)

        # Iterating: The current prediction becomes the base for the next power
        A = predict_A

        # Verify if the Law holds true
        print(predict_A == actual_A)



if __name__ == "__main__":
    verify_julian_first_law(B=5, k=2,n=10)