import os
files = [a.replace(".py", "") for a in os.listdir(os.getcwd()) if ".py" in a]
filtered_files = [a for a in files if not any([k in a for k in ("all_files", "_test", "manage", "utils")])]
for m in filtered_files:
    locals()[m] = __import__(m)