import quick_cli as qc

print("I'm not impacted!")
print(f"""You selected {qc.select_menu(["APPLE", "ORANGE", "BANANA", "PEAR"])}.""")
print("I'm still visible!")