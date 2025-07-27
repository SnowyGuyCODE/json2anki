import json
import os

filename = "data.txt"
prompt = "Only a COMPATIBLE operating system is COMPATIBLE with this python script.\nAre you using a COMPATIBLE operating system right now? (yes/no): "

def json_to_anki(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    words = data.get("da-en", {})
    
    # Prepare Anki lines
    lines = []
    for word, details in words.items():
        translation = details.get("translation", "")
        lines.append(f"{word}\t{translation}")
    
    # Save as TXT
    out_path = os.path.splitext(json_path)[0] + "_anki.txt"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))
    
    print(f"✅ Converted JSON → Anki TXT: {out_path}")
    os.system("color a")
    os.system("pause>nul")
    os.system("color 07")

def warn():
    if os.path.exists(filename):
        with open(filename, "r") as f:
            saved_answer = f.read().strip().lower()
        
        if saved_answer == "yes":
            main()
        elif saved_answer == "no":
            answer2 = input(prompt).strip().lower()
            if answer2 == "yes":
                with open(filename, "w") as f:
                    f.write(answer2)
                print("Answer saved:", answer2)
                main()
            elif answer2 == "no":
                print("Exiting program. This script requires a COMPATIBLE operating system.")
                exit()
            else:
                print("Invalid input. Please run the program again.")
                exit()
        else:
            print(f"Unexpected saved answer '{saved_answer}'. Please delete '{filename}' and try again.")
            exit()
    else:
        answer = input(prompt).strip().lower()
        if answer in ["yes", "no"]:
            with open(filename, "w") as f:
                f.write(answer)
            print("Answer saved:", answer)
            if answer == "yes":
                main()
            else:
                print("Exiting program. This script requires a COMPATIBLE operating system.")
                exit()
        else:
            print("Invalid input. Please run the program again.")
            exit()

def main():
    os.system("cls")
    os.system("color 07")
    print("INSTRUCTIONS:\n1. Insert the JSON file into this directory ('json2anki')\n2:", end=" ")
    file_path = input("Enter the JSON file -> ").strip()
    
    if not os.path.exists(file_path):
        if file_path == "IncompatibleErrorFix":
            print("❌ Change the answer value in 'data.txt'.")
            os.system("color c")
            os.system("pause>nul")
            os.system("color 07")
            exit()
        else:
            print("❌ File not found.")
            os.system("color c")
            os.system("pause>nul")
            os.system("color 07")
            exit()
    
    if file_path.lower().endswith(".json"):
        json_to_anki(file_path)
    else:
        if file_path == "IncompatibleErrorFix":
            exit()
        else:
            print("❌ Unsupported file type. Use '.json'.")
            os.system("color c")
            os.system("pause>nul")
            os.system("color 07")

if __name__ == "__main__":
    warn()
