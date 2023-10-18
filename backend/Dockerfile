# Utiliser une image Python officielle comme image de base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY app.py .

# Installer the dependencies
RUN pip install Flask
RUN pip install Werkzeug
RUN pip install flask-cors

# Exposer le port sur lequel l'application s'exécutera
EXPOSE 8000

# Commande pour exécuter l'application
CMD ["python", "app.py"]
