from src.recommender import MusicRecommender


def main():
    recommender = MusicRecommender("data/songs.csv")

    print("🎵 Music Recommender Ready!")

    # Example preferences
    preferences = {
        "genre": "lofi",
        "mood": "chill"
    }

    results = recommender.recommend(preferences)

    print("\nTop Recommendations:")
    for song in results:
        print(f"{song['title']} by {song['artist']}")


if __name__ == "__main__":
    main()
