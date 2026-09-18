assets = []
asset_types = ["Workstation", "Server", "Router", "Switch", "Application"]
risk_levels = ["Low", "Medium", "High", "Critical"]
security_status = ["Secure", "Warning", "Vulnerable"]


def add_asset():
    print("\n--- Add Asset ---")
    asset = {}

    asset["id"] = input("Asset ID: ")
    asset["name"] = input("Asset Name: ")

    while True:
        asset["type"] = input("Asset Type (Workstation/Server/Router/Switch/Application): ")
        if asset["type"] in asset_types:
            break
        print("Invalid Asset Type!")

    asset["ip"] = input("IP Address: ")
    asset["os"] = input("Operating System: ")
    asset["department"] = input("Department: ")

    while True:
        asset["risk"] = input("Risk Level (Low/Medium/High/Critical): ")
        if asset["risk"] in risk_levels:
            break
        print("Invalid Risk Level!")

    while True:
        asset["status"] = input("Security Status (Secure/Warning/Vulnerable): ")
        if asset["status"] in security_status:
            break
        print("Invalid Security Status!")

    assets.append(asset)
    print("Asset Added Successfully!\n")


def search_asset():
    aid = input("Enter Asset ID to search: ")
    for a in assets:
        if a["id"] == aid:
            print("\nAsset Found")
            display_single(a)
            return
    print("Asset Not Found!")


def update_asset():
    aid = input("Enter Asset ID to update: ")
    for a in assets:
        if a["id"] == aid:
            print("Leave blank to keep old value.")

            name = input(f"Asset Name ({a['name']}): ")
            if name:
                a["name"] = name

            ip = input(f"IP Address ({a['ip']}): ")
            if ip:
                a["ip"] = ip

            os = input(f"Operating System ({a['os']}): ")
            if os:
                a["os"] = os

            dept = input(f"Department ({a['department']}): ")
            if dept:
                a["department"] = dept

            risk = input(f"Risk Level ({a['risk']}): ")
            if risk in risk_levels:
                a["risk"] = risk

            status = input(f"Security Status ({a['status']}): ")
            if status in security_status:
                a["status"] = status

            print("Asset Updated Successfully!")
            return
    print("Asset Not Found!")


def delete_asset():
    aid = input("Enter Asset ID to delete: ")
    for a in assets:
        if a["id"] == aid:
            assets.remove(a)
            print("Asset Deleted Successfully!")
            return
    print("Asset Not Found!")


def display_single(a):
    print("-----------------------------------------")
    print("Asset ID    :", a["id"])
    print("Asset Name  :", a["name"])
    print("Asset Type  :", a["type"])
    print("IP Address  :", a["ip"])
    print("OS          :", a["os"])
    print("Department  :", a["department"])
    print("Risk Level  :", a["risk"])
    print("Status      :", a["status"])


def display_assets():
    print("\n=========================================")
    print(" CYBERSECURITY ASSET INVENTORY")
    print("=========================================")

    if not assets:
        print("No Assets Available!")
        return

    critical = high = medium = vulnerable = 0

    for a in assets:
        display_single(a)

        if a["risk"] == "Critical":
            critical += 1
        elif a["risk"] == "High":
            high += 1
        elif a["risk"] == "Medium":
            medium += 1

        if a["status"] == "Vulnerable":
            vulnerable += 1

    print("=========================================")
    print("Total Assets      :", len(assets))
    print("Critical Assets   :", critical)
    print("High Risk Assets  :", high)
    print("Medium Risk Assets:", medium)
    print("Vulnerable Assets :", vulnerable)
    print("=========================================")

while True:
    print("\n===== CYBERSECURITY ASSET INVENTORY =====")
    print("1. Add Asset")
    print("2. Search Asset")
    print("3. Update Asset")
    print("4. Delete Asset")
    print("5. Display All Assets")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_asset()
    elif choice == "2":
        search_asset()
    elif choice == "3":
        update_asset()
    elif choice == "4":
        delete_asset()
    elif choice == "5":
        display_assets()
    elif choice == "6":
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!")
