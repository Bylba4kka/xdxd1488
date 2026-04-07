
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
    python -m venv venv
    ```

4. Установить зависимости 
    ```bash
    pip install -r requirements.txt
    ```

5. Запустить проект  
    ```bash
    uwsgi --ini uwsgi.ini
    ```

6. Устанавливаем nginx 
    ```bash
    sudo apt-get update && sudo apt-get install nginx
    ```

7. Созданиём конфигурацию для проекта `sudo nano /etc/nginx/sites-available/django_form_handler` и вставляем:
    ```
    server {
        listen 80;

        server_name YOUR_SERVER_IP;

        location / {
            include uwsgi_params;
            uwsgi_pass unix:/UWSGI_PASS;
        }
    }

    ```

    Где,

    YOUR_SERVER_IP - IP виртуальной машины (например 123.45.67.89/)
    UWSGI_PASS - полный путь к сокету uWSGI (например /home/django_form_handler/project.sock)

