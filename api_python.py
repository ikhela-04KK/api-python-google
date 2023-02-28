import os 
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build



"""
demarer avec un autre cmd
ajouter un dossier dans une session nviTree déjà ouverte fdfd
"""


#informations reccurentes 
API_SERVICE_NAME = 'youtube' 
API_VERSION = 'v3'

#definir une variable d'environnement dans notre projet afin de ne pas pouvoir avoir accès visiblement à ça 
API_KEY = os.environ.get('YT_API_KEY')
print(API_KEY)

# continue à suivre les autres videos pour avoir une idée de ce qui se passe 
# API_KEY = 'AIzaSyCcIT18qLpYWN_Xcegvrke77_nJRvwlttY'#! la clé doit être changer 



# il n'y a pas d'autorisation donc ça ne fonctionne pas , il faut que je puisses avoir les autorisation neccessaire afin
# # Construit une requête pour accéder à la YouTube Data API

#informations d'authentifications 
flow = InstalledAppFlow.from_client_secrets_file("./ytikhe_ytNew.json",scopes=["https://www.googleapis.com/auth/youtube-readonly","https://www.googleapis.com/auth/youtubepartner","https://www.googleapis.com/auth/youtubepartner-channel-audit"])
flow.run_local_server(port=4574,prompt="consent")

credentials = flow.credentials  #il n' y a pas de parenthèse 
print(credentials.to_json())


# youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)
# pl_channel=youtube.playlistItems().list(
#     part='status',
#     # maxResults=50
#     playlistId='PLzMcBGfZo4-ndH9FoC4YWHGXG5RZekt-Q'
# )
# pl_execute = pl_channel.execute()
# print(pl_execute)
# # # ajout de static_discovery pour s'aasurer que les informations les plus à jour sont utilisés 
# # #*recupperer les informations de ça chaînes youtbe 
# # request = youtube.activities().list(
# #     part='statistics',
# #     forUsername='kan koffi'
# # )
# # response=request.execute()
# # print(response)
# # #*pour faire appelle à ça chaîne youtube 
# # #*Récupère la liste de vidéos de l'historique de visionnage
# # request = youtube.activities().list(part="id",
# #                                     home=True,
# #                                     maxResults=50)
# # response = request.execute()
# # # Affiche les titres des vidéos de l'historique de visionnage
# # for item in response["items"]:
# #     video_id = item["id"]["videoId"]
# #     video_request = youtube.videos().list(part="snippet", id=video_id)
# #     video_response = video_request.execute()
# #     video_title = video_response["items"][0]["snippet"]["title"]
# #     print(video_title)
