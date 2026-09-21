import os


def analyze_folder(folder):
    if not os.path.isdir(folder):
        return None

    results = []

    for root, _, files in os.walk(folder):
        for filename in files:
            path = os.path.join(root, filename)

            try:
                size = os.path.getsize(path)
                relative = os.path.relpath(path, folder)
                size_kb = round(size / 1024, 2)

                results.append((relative, size_kb))

            except OSError:
                continue

    results.sort(key=lambda item: item[1], reverse=True)

    return results
