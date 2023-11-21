import requests
from PIL import Image
from io import BytesIO

class NASAAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.nasa.gov"

    def get_apod(self):
        endpoint = "/planetary/apod"
        url = f"{self.base_url}{endpoint}?api_key={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def show_apod_image(self):
        apod_data = self.get_apod()
        if apod_data:
            print("Informasi Astronomi Foto Hari Ini (APOD):")
            print("Title:", apod_data.get('title'))
            print("Date:", apod_data.get('date'))
            print("Explanation:", apod_data.get('explanation'))
            print("URL:", apod_data.get('url'))

            # Menampilkan gambar
            image_url = apod_data.get('url')
            response = requests.get(image_url)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                image.show()
            else:
                print("Gagal mendapatkan gambar.")
        else:
            print("Gagal mendapatkan data APOD.")
