# HistoireDeFrance

setup :
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

lancer le docker :
docker compose up --build  # la premiere fois
docker compose up # si pas besoin de rebuild