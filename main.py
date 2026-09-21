from analyzer import analyze_folder

print("📦 Folder Size Map")
print("=" * 40)

folder = input("Enter folder path: ").strip()

results = analyze_folder(folder)

if results is None:
    print("❌ Folder not found.")
elif not results:
    print("📭 No files found.")
else:
    print("\n📊 Files by size:\n")

    for name, size in results:
        print(f"{size:>10} KB  {name}")
