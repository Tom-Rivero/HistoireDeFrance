# HistoireDeFrance

setup :
python3.11 -m venv venv
source venv/bin/activate
pip install .

lancer le docker :
docker compose up --build  # la premiere fois
docker compose up # si pas besoin de rebuild


Idée en +:
Stocker les questions mal répondues pour les reposer plus tard
RAG avec base de connaissance (liée à Wikipedia ou autre) pour gagner en fiabilité sur les infos, et si on veut garantir le scope des questions
Mode examen + stockage des résultats ?

