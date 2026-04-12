def find_similar_numbers(base, k):
    results = []
    for i in range(2, base):
        # Checking if the last k digits remain invariant when squared
        if (i ** 2) % (10 ** k) == i % (10 ** k):
            results.append(i)
    return results

if __name__ == "__main__":
    print(find_similar_numbers(100, 2))