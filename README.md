# devops-todo-app

#add below env in .env files
Database Configuration
DB_HOST=15.207.249.132
DB_PORT=3306
DB_NAME=devops_todo
DB_USER=root
DB_PASSWORD=suraj559

Flask Security
SECRET_KEY=eW91cl92ZXJ5X3N0cm9uZ19zZWNyZXRfa2V5X2hlcmU=

docker run -itd -p 5000:5000 --env-file .env <imageName>
