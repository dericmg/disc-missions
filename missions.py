import os

appdata_path = os.getenv('APPDATA')
settings_path = os.path.join(appdata_path, 'discord', 'settings.json')
new_key = '"DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING": true,'

try:
    with open(settings_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    file_content = "".join(lines)

    if "DANGEROUS_ENABLE_DEVTOOLS" not in file_content:
        indentation = "  "
        new_line = f"{indentation}{new_key}\n"
        lines.insert(1, new_line)

        with open(settings_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        print("Line inserted successfully.")
    else:
        print("Key already exists in file.")

except Exception as e:

    print(f"Error: {e}")
