
Деплой на линукс сервер

cd /home/
sudo apt install && sudo apt upgrade -y
sudo snap refresh 

1. Скачать python `sudo apt-get update && sudo apt-get install python3`

2. Клонировать репозиторий в папку `./home/`
    ```bash
    git clone https://github.com/Bylba4kka/xdxd1488.git
    ```

3. Создать виртуальное окружение 
    ```bash
    python3 -m venv venv
    ```

4. Установить зависимости 
    ```bash
    pip install -r requirements.txt
    ```

создаем папку для сокета
mkdir -r /run/uwsgi



6. Устанавливаем nginx 
    ```bash
    sudo apt-get update && sudo apt-get install nginx
    ```

7. Созданиём конфигурацию для проекта `sudo nano /etc/nginx/sites-available/django_form_handler` и вставляем:
    ```
    server {
        listen 1488;

        server_name YOUR_SERVER_IP;

        location / {
            include uwsgi_params;
            uwsgi_pass unix:/run/uwsgi/project.sock;
        }
    }

    ```

    Где,

    YOUR_SERVER_IP - IP виртуальной машины (например 123.45.67.89)
    ip addr show (inet)



символическая ссылка
sudo ln -s /etc/nginx/sites-available/django_form_handler/etc/nginx/sites-enabled/

проверка конфигурации
sudo nginx -t

перезапускам 
sudo systemctl restart nginx

добавляем в  django_form_handler/settings.py в ALLOWED_HOSTS наш айпи сервера



настравиваем БД

sudo apt install postgresql postgresql-contrib -y

sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo systemctl status postgresql 


создаем бд и пользователя
CREATE USER myuser WITH PASSWORD '123321';
CREATE DATABASE db OWNER myuser;
GRANT ALL PRIVILEGES ON DATABASE db TO myuser;


делаем переменные окружения
export DB_USER="user"
export DB_PASS="123321"
export DB_NAME="database"
export DB_HOST="db"
export DB_PORT="5432"


5. Запустить проект  
    ```bash
    uwsgi --ini uwsgi.ini --daemonize uwsgi.log
    ```


