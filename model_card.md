## 1. Model Name  

**VibeMatcher 1.0**  

---

## 2. Intended Use  

This recommender suggests music songs based on what genre, mood, and energy level you like. It assumes users have clear preferences for these three things. It's made for classroom learning, not for real users on a music app.  

---

## 3. How the Model Works  

The system looks at each song's genre, mood, and energy. It compares these to what the user wants. If the genre matches, it adds 1 point. Same for mood. For energy, it calculates how close the song's energy is to the user's preference and multiplies that by 2. The total score decides the top recommendations. I changed the weights to make energy more important than the starter code.  

---

## 4. Data  

The dataset has 18 songs. It includes genres like pop, rock, ambient, electronic, and more. Moods range from happy to intense to chill. Energy levels go from 0.28 to 0.95. I added 8 more songs to the original 10. The dataset misses some tastes, like very low energy or specific sub-genres.  

---

## 5. Strengths  

The system works well for users with strong preferences in one area, like high energy rock fans. It captures energy matching pretty accurately. Recommendations often match intuition when preferences are straightforward.  

---

## 6. Limitations and Bias 

The energy closeness formula (1 - |song_energy - user_energy|) creates a filter bubble for users with extreme energy preferences, such as very low (e.g., 0.1 for calm ambient) or very high (e.g., 0.95 for intense metal), because the dataset's energy values range mostly from 0.28 to 0.95, leading to inherently lower maximum scores for these users and potentially repetitive or less satisfying recommendations. This unfairly disadvantages users who prefer niche energy levels not well-represented in the catalog, as the system can't provide close matches, forcing reliance on genre or mood alone. Additionally, the small dataset (18 songs) amplifies this bias, limiting overall diversity and making it harder to evaluate edge cases. To address this, future improvements could include energy normalization or dataset expansion with more varied energy levels.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

I tested the recommender with several different user profiles to see how it handled various tastes. These included a "Happy Pop Lover" who likes upbeat pop music with medium-high energy, a "Gym Hero" profile for high-energy electronic tracks, a "Chill Ambient Fan" for calm, low-energy ambient music, a "Rock Enthusiast" for energetic rock, and a "Sad Ballad Seeker" for mellow pop ballads. I also ran some tricky "adversarial" tests with conflicting preferences, like wanting high-energy pop but with a sad mood, to see how the system would cope.

What surprised me most was that the song "Gym Hero" kept showing up in recommendations for people who just wanted "Happy Pop" music. "Gym Hero" is actually a high-energy, intense pop song, not really happy or chill. The reason this happens is that our scoring system gives a lot of weight to how close the song's energy level is to what the user wants. Even if the mood doesn't match at all, a song with very similar energy gets a big boost in its score. So, for someone looking for happy pop at energy level 0.8, "Gym Hero" at 0.93 energy scores high because the energy difference is small, outweighing the mood mismatch. It's like the system is saying "close enough on energy" and ignoring the mood, which can lead to unexpected recommendations that don't quite fit the vibe the user is after.

---

## 8. Future Work  

Add more song features like tempo or danceability. Make recommendations more diverse by avoiding repeats. Explain scores better to users. Handle mixed tastes, like wanting both happy and sad songs.  

---

## 9. Personal Reflection  

My biggest learning moment was realizing how small changes in scoring weights can create unexpected biases, like the energy filter bubble. It showed me that even simple systems need careful testing to avoid unfair results.  

Using AI tools like GitHub Copilot helped a lot with writing code quickly and suggesting fixes, but I had to double-check the logic for scoring and data loading to make sure it matched what I wanted.  

What surprised me was how a basic weighted matching algorithm could still produce recommendations that felt personalized and useful, even without complex machine learning.  

If I extended this project, I'd try adding user feedback loops to adjust weights dynamically and incorporate more song features like lyrics or artist popularity.  
