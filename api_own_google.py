
# actuellement je suis les videos afin de mieux comprendre les proccessus eet de faire en sorte de m'inprgner d ela situation
from googleapiclient.discovery import build
#import os
import re 
from datetime import timedelta
from pytube import YouTube
# from dotenv import load_dotenv

"""
activer la sauvegarde automatique 
creer une fonction qui transforme l'id d'une video en nom:ok
je dois inserer les barres de téléchargement , pour qu'il me montre la duréée du téléchargement en cours: ok
il y'a une partie ou l'on peut reccuperer les tailles des videos 
est ce que je vais pas combiner avec un dictionaire je me dis que ça sera mieux 
mettre ça clé dans un environnement c'est mieux :ok
"""




#début de la construction 
api_key = "AIzaSyClWLgcJQMhWu3BzDo9Ks7lvfSkgm_nT-w"
# AIzaSyClWLgcJQMhWu3BzDo9Ks7lvfSkgm_nT-w
youtube = build('youtube', 'v3',developerKey=api_key)

                        # request = youtube.channels().list(    
                        #     part='statistics',
                        #     forUsername='kan koffi'
                        # )
                        #cette requête permet de voir la liste des playistes dont on dispose 
                        #channels().list() pour les informations sur la chaîne
                        #playlists().list() pour la voir les élements et toutes les playlists qu'il y' sur 
#implementer la boucle pour voir la liste des videos sur toutes playist 
#* determiner la duréé des video grâce à  des expresiion regex
heure_pattern = re.compile(r'(\d+)H')
minute_pattern = re.compile(r'(\d+)M')
seconde_pattern = re.compile(r'(\d+)S') 
nextPageToken = None
total_seconds=0



#cette fonction permet de reccuperer le nom d'une video venant d'une playlist
def nameVideo(id_video):
    pl_names,video_names =[],[]
    vi_id = youtube.videos().list(
        part="snippet",
        id =",".join(id_video) 
    ).execute()

    #plalist_name 
    #pl_name = youtube.videos().list(
    #    part="channelTitle",
    #    id=",".join(id_video)
    #).execute()
    for i in range(len(id_video)):
         video_name = vi_id['items'][i]['snippet']['title']
         pl_name = vi_id['items'][i]['snippet']['channelTitle']
         pl_names.append(pl_name)
         video_names.append(video_name)
    return video_names,pl_names
    # print(video_name,"la playlist est: \n",pl_name)

#debut de creation de la fonction qui permet de telarger la liste des videos des playlists que j'ai en ma possesion 
def downloads_playlist(id_videos,videos,playlists):#appelle de la playlist downloads_playlist(id_video())
    for id_video,video,playlist in zip(id_videos,videos,playlists):
        tag = input(f"""
                    Veux tu télécharger ?
                    Playlist:{playlist}
                    Video:{video}
                    """)  # cette video doit être mis dans tkinter genre un trucs de choix  
        if tag=="oui":
            video_link = f"https://www.youtube.com/watch?v={id_video}"
            #creation d'une instance de la video 
            youtube = YouTube(video_link)
        
            #prendre la plus hautre resolution 
            video =youtube.streams.get_highest_resolution()
        
            #le dossier de télechargement
            path = "C:\\Users\\ikhela\\videos\\"
        
            #telecharger les videos et la progress bar ²
            #video.download(output_path=path)
            video.on_progress = lambda chunk, file_handle, bytes_remaining: tqdm.update("{:.2f} %".format((1-bytes_remaining/stream.filesize)*100))
            video.download(output_path=output_path, filename=stream.default_filename)

                        
    


#!determiner les liens des videos youtube


while True:
    pl_request = youtube.playlistItems().list(
        part='contentDetails', # l'ajout d snippet permet de voir plus de details 
                            # forUsername='ikhe',     pour channels()
                            # channelId="UCsy7lcLpwSDbndC2KCgsaMQ" #mettre le code du channel voici le code de ma chaîne , il y' a differentes video que je 
        playlistId="PLzMcBGfZo4-kR7Rh-7JCVDN8lm3Utumvq",  #ça c'est id d'une playiste afin de voir les éléments qui y sont à l'intérieur 
        
        # PLZK6b9si4D4S_gV46ejjkPfvwj_NxV0Mh
        maxResults = 50,
        pageToken=nextPageToken
    )
    pl_reponse = pl_request.execute()
    #print(pl_reponse)


    print()
    print()
    print("test")
    #pour resinder sur les informations
    
    #fonction qui retourne l'id d'une playist
    def video_ids():
        vid_ids=[]
        for item in pl_reponse['items']:
            vid_id=item['contentDetails']['videoId']
            # print(item['contentDetails'])
            vid_ids.append(vid_id)
        return vid_ids

    #voir les ressources de chaque video dans la playist 
    vid_request = youtube.videos().list(
        part='contentDetails',
        id=','.join(video_ids())
    )
        #séparer les identifiants par les des virgule)
    vid_reponse = vid_request.execute()
    # print(vid_reponse) #pour voir le contenu des ids des videos 


    #pour voir la durée des videos uniquement
    for item in vid_reponse['items']:
        duration = item['contentDetails']['duration']
                            #print(duration)
        heure= heure_pattern.search(duration) # duration =PT21H7M01S 
        minute=minute_pattern.search(duration)
        seconde=seconde_pattern.search(duration)
        
        heure = int(heure[1]) if heure else 0
        minute = int(minute[1]) if minute else 0
        seconde = int(seconde[1]) if seconde else 0

        #utilisation de timedlta pour convertir toute les temps en seconde 
        video_seconds = timedelta(
            hours=heure,
            minutes=minute,
            seconds=seconde
        ).total_seconds()
                            #print(duration) affiche la durrée de chaque video 
                            #print(heure,'heure ',minute,'minute ',seconde,'seconde ')
        total_seconds += video_seconds
        
    #page à la page suivante
    nextPageToken = pl_reponse.get('nextPageToken')
    
    #sort de la boucle s'il ne trouve plus de page 
    if not nextPageToken:
        break

videos,playlists = nameVideo(video_ids())
downloads_playlist(video_ids(),videos,playlists)

total_seconds = int(total_seconds)
minute,secondes = divmod(total_seconds,60)
heure,minute = divmod(minute,60)
print(f'{heure}:{minute}:{secondes}')


#implementer une fonction pour telecharger directement les videos de ta playist 

