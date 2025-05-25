#for playing songs

import yt_dlp
import vlc

def music (text):
    print("Wait for a few seconds...")
    search = f"ytsearch:{text}"  # ✅ This defines the variable

    ydl_opts = {
        'format': 'bestaudio',
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search, download=False)
        entries = info.get('entries', [])

    if len(entries) > 1:
        
        video_url = entries[1]['url']  # Use second result
        print("Playing your song 😊")
    elif len(entries) == 1:
        
        video_url = entries[0]['url']  # Fallback to first result
        print("Playing your song 😊")
    else:
        print("❌ No matching songsfound.")
        return

    player = vlc.MediaPlayer(video_url)
    player.play()

    input("Press Enter to stop playing the song")

    player.stop()
    print("Song stopped.")

    
   