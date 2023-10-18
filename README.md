# kubernetes_project
Nom de projet : Projet : Application Web Microservices avec Kubernetes

Par rapport à l’application,
Back end : API avec Flask
docker build -t myflaskapp:latest .
docker run -d --name myflaskapp-container -p 8000:8000 myflaskapp:latest
Frontend (Application React): en utilisant le node js et le react 
docker build -t frontend-image .
docker run -d -p 3001:80 --name frontend-container frontend-image
Pour le back et le front, chacun a un docker à exécuter 

Après avoir les deux conteneurs (front et back) fonctionne correctement, c’est 
la partie de kubernetes;
L’environnemnet de kubernetes locale : minikube 

Pour lancer kubernetes en locale: 
minikube start
minikube addons enable ingress
kubectl apply -f myflaskapp-deployment.yaml
kubectl apply -f myflaskapp-service.yaml
kubectl apply -f frontend-deployment.yaml
kubectl apply -f frontend-service.yaml
kubectl apply -f ingress.yaml
