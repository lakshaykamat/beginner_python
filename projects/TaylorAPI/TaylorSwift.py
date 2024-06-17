import requests


class TaylorSwift:
    def __init__(self, base_url):
        self.base_url = base_url

    def _make_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()

    def get_albums(self) -> list[dict]:
        return self._make_request(f"albums")

    def get_album(self, name) -> dict:
        return self._make_request(f"albums/{name}")

    def get_songs(self) -> list[dict]:
        return self._make_request("songs")

    def get_lyric_of_song(self, song_name: str) -> str:
        song = self._make_request(f"songs/{song_name}")
        return song["lyrics"].strip()
