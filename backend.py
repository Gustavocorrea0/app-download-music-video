import yt_dlp

def download_music(url_video, path_video):
    try:
        path_save_video = f'{path_video}/' + '%(title)s.%(ext)s'
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': path_save_video,  
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url_video])

        return True
    except Exception as ex:
        return False

def download_video(url_video, path_video):
    try:
        path_save_video = f'{path_video}/' + '%(title)s.%(ext)s'
        
        ydl_opts = {
            'format': 'best',
            'outtmpl': path_save_video, 
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url_video])

        return True
    except Exception as ex:
        return ex