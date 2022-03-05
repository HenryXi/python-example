even_numbers = list(range(2, 11, 3))
print(even_numbers)

version = "V.sds"
if version.endswith(".110816") or version.endswith(".PRELOAD") or version.endswith(".DEV") or not version.startswith("V"):
    print("ignore")
else:
    print("handle")
