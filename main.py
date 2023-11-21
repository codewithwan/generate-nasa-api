from nasaapi import NASAAPI

def main():
    # Ganti 'YOUR_API_KEY' dengan API key NASA yang valid
    api_key = 'YOUR_API_KEY'
    nasa = NASAAPI(api_key)
    nasa.show_apod_image()

if __name__ == "__main__":
    main()
