import json


def display_results(results):

    print("\n========== Scan Results ==========\n")

    for result in results:

        print(f"Port    : {result['port']}")
        print(f"Service : {result['service']}")
        print(f"Banner  : {result['banner']}")

        print("-" * 35)

    print(f"\nTotal Open Ports : {len(results)}")


def save_json_report(results):

    filename = "scan_results.json"

    with open(filename, "w") as file:

        json.dump(results, file, indent=4)

    print("\nJSON report saved successfully.")
    
    print(f"Saved as : {filename}")