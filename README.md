# 🎵 Custom MP3 Player

A modern, fully functional MP3 Player built from scratch using Python and PyQt6. This application features a custom-designed graphical user interface (GUI) and robust background logic for handling audio playback and playlist management.

## Key Features

* **Audio Playback:** Play, Pause, Next, and Previous functionality.
* **Advanced Playback Modes:** * **🔀 Shuffle:** Generates an randomized queue to ensure no repeated songs until the playlist ends.
    * **🔁 Repeat:** Loops the currently playing track.
* **Playlist Management (CRUD):**
    * Create new custom playlists.
    * Add local audio files (`.mp3`, `.wav`, `.ogg`) to specific playlists.
    * Delete individual songs or entire playlists.
    * Persistent storage: Playlists and their contents are automatically saved to a local `JSON` file, so your music is always there when you restart the app.
* **Dynamic UI Controls:**
    * Interactive volume slider with mute toggle.
    * Real-time song progress bar (slider) with exact duration tracking.
    * Custom CSS styling with dynamic hover and active states for all buttons.

## Technologies Used
* **Python 3**
* **PyQt6** (for the Graphical User Interface)
* **JSON** (for data persistence)
* **Custom Audio Engine** (`player_engine.py` handling backend audio processing)

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Diana141004/MP3-Player.git
2. Install the required dependencies:
 ```bash
   pip install -r requirements.txt
```
3. Run the application:
```bash
   python main.py
```


Icons design made by https://github.com/Revfem
* For songs, check this site where you can download mp3 files and upload them in the project by pressing the button "add Song": https://mp3juice.as/ 
