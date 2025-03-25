def get_secret(secret_name):
    try:
        with open(f"/run/secrets/{secret_name}", "r", encoding="utf-8-sig") as secret_file:
            # utf-8-sig encoding automatically handles the BOM
            return secret_file.read().strip()
    except Exception as e:
        print(f"Error reading secret {secret_name}: {e}")
        return None