import json


def display_results(

        results,
        target,
        total_ports,
        scan_time

):

    print("\n========== PortSentinel Scan Summary ==========\n")

    print(f"Target            : {target}")
    print(f"Ports Scanned     : {total_ports}")
    print(f"Open Ports        : {len(results)}")
    print(f"Scan Time         : {scan_time} seconds")

    print("\n----------------------------------")

    for result in results:

        print(f"\nPort      : {result['port']}")
        print(f"Service   : {result['service']}")
        print(f"Banner    : {result['banner']}")

        certificate = result.get("certificate")

        if certificate:

            print("\nTLS Certificate Information")

            print(
                f"Valid From : "
                f"{certificate['valid_from']}"
            )

            print(
                f"Valid Until : "
                f"{certificate['valid_until']}"
            )

            print(
                f"Issuer : "
                f"{certificate['issuer']}"
            )

        print("\n----------------------------------")
        
def save_json_report(results):

    filename = "scan_results.json"

    with open(filename, "w") as file:

        json.dump(results, file, indent=4)

    print("\nJSON report saved successfully.")
    
    print(f"Saved as : {filename}")