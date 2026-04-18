## 1. Model Name
VibeFinder 1.0

## 2. Intended Use
This recommender suggests songs based on user preferences like genre and mood. It is designed for classroom exploration, not real-world deployment.

## 3. How the Model Works
The model reads a dataset of songs from a CSV file and compares song attributes (genre, mood, energy, etc.) with user preferences. It returns songs that best match those preferences.

## 4. Example Inputs
- genre: lofi
- mood: chill

## 5. Example Outputs
- Sunrise City by Neon Echo
- Midnight Coding by LoRoom
- Storm Runner by Voltiline

## 6. Limitations
The model uses a small dataset and simple matching logic. It may not generalize well and may return less accurate results for vague or uncommon preferences.

## 7. Risks / Biases
The model’s recommendations depend entirely on the dataset. If the dataset lacks diversity in genres or artists, the recommendations will reflect that bias. 
