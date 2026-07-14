def display_results(results):

    print("\n========== Scan Results ==========\n")

    for result in results:

        print(f"Port    : {result['port']}")
        print(f"Service : {result['service']}")
        print(f"Banner  : {result['banner']}")

        print("-" * 35)