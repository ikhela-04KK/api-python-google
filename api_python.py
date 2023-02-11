from googleapiclient.discovery import build
# import google.auth
#informations reccurentes 
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
API_KEY = 'AIzaSyA-MDgI4A-4u732INHWA0AzlzUnt-lV86U'

# creds, _ = google.auth.default()
# ,static_discovery=False
# Construit une requête pour accéder à la YouTube Data API
youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)
# ajout de static_discovery pour s'aasurer que les informations les plus à jour sont utilisés 

# Récupère la liste de vidéos de l'historique de visionnage
request = youtube.activities().list(part="id",
                                     home=True,
                                     maxResults=50)
response = request.execute()

# Affiche les titres des vidéos de l'historique de visionnage
for item in response["items"]:
    video_id = item["id"]["videoId"]
    video_request = youtube.videos().list(part="snippet", id=video_id)
    video_response = video_request.execute()
    video_title = video_response["items"][0]["snippet"]["title"]
    print(video_title)