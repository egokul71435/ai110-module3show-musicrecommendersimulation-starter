"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def test_adversarial_profiles():
    """Temporary function to test adversarial user profiles."""
    songs = load_songs("data/songs.csv") 

    # Adversarial profiles for testing edge cases
    profiles = [
        ("High energy pop with sad mood (conflicting)", {"genre": "pop", "mood": "sad", "energy": 0.9, "likes_acoustic": False}),
        ("Low energy rock with chill mood (conflicting)", {"genre": "rock", "mood": "chill", "energy": 0.1, "likes_acoustic": False}),
        ("Non-existent genre/mood with acoustic preference", {"genre": "nonexistent", "mood": "nonexistent", "energy": 0.5, "likes_acoustic": True}),
    ]

    for name, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print(f"\n{name}:")
        for rec in recommendations:
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f} - {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
    # test_adversarial_profiles()

