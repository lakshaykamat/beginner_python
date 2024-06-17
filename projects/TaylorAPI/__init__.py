import requests
from TaylorSwift import TaylorSwift


def compare_lyrics_with_sentence(lyrics: str, sentence: str):
    # Convert both the lyrics and the sentence to lowercase for case-insensitive comparison
    lyrics_lower = lyrics.lower()
    sentence_lower = sentence.lower()

    # Check if the sentence is present in the lyrics
    if sentence_lower in lyrics_lower:
        return True
    else:
        return False


if __name__ == "__main__":
    API_BASE_URL = "https://taylor-swift-api.vercel.app/api"
    taylor_swift_api = TaylorSwift(API_BASE_URL)

    try:    
        print(taylor_swift_api.get_album(input("Album name: ")))

    except requests.RequestException as e:
        print(f"Error: {e}")
