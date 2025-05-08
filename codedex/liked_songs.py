
liked_songs = {
    "Perfect": "Ed Sheeran",
    "Stress out": "Twenty one pilots",
    "Runaway": "Kendrick laamar",
    "Uptown Funk": "Mark Ronson ft. Bruno Mars",
}

# Function to display and write liked songs to a file
def write_liked_songs_to_file(songs, file_name):
    with open(file_name, 'w') as file:
        file.write("Liked Songs:\n")
        for song, artist in songs.items():
            file.write(f"{song} by {artist}\n")
    print(f"Successfully added Liked songs to {file_name} ❤️")

# Write liked songs to a .txt file
write_liked_songs_to_file(liked_songs, "liked_songs.txt")