district_codes = {
    "vizag": "AP-31",
    "visakhapatnam": "AP-31",
    "vijayawada": "AP-16",
    "guntur": "AP-07",
    "nellore": "AP-26",
    "tirupati": "AP-03",
    "kurnool": "AP-21",
    "anantapur": "AP-02",
    "kadapa": "AP-04",
    "rajahmundry": "AP-05",
    "eluru": "AP-37",
    "ongole": "AP-27",
    "srikakulam": "AP-30",
    "vizianagaram": "AP-35"
}

district = input("Enter district name: ").strip().lower()

if district in district_codes:
    print("Vehicle registration code is:", district_codes[district])
else:
    print("District not found")
output:-
Enter district name: vizag
Vehicle registration code is: AP-31

=== Code Execution Successful ===


