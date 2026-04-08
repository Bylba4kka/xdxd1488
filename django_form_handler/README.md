## О Приложении

Создание формы с возможностью динамического добавления полей ввода с помощью jQuery, не привязанной к конкретной модели. При нажатии на кнопку «Добавить» форма добавляет новый поле ввода с уникальным именем (например, name, name1, name2 и т.д.).

Сохранение всех введённых значений из динамических полей в модели в поле типа JSONB в базе данных PostgreSQL, чтобы данные хранились в формате JSON.

Отображение сохранённых данных в отдельном представлении (вьюсе), где форма показывает все значения, отправленные пользователем, извлечённые из поля JSON.

## Деплой на линукс сервер

1. Обновить пакеты и скачать Python
    ```bash
    sudo apt install && sudo apt upgrade -y
    sudo snap refresh 
    sudo apt-get install python3
    ```

2. Перейти в домашнюю директорию
   ```bash
   cd /home/
   ```

3. Клонировать репозиторий в папку `./home/`
    ```bash
    git clone https://github.com/Bylba4kka/xdxd1488.git
    ```

4. Создать виртуальное окружение 
    ```bash
    python3 -m venv venv
    ```

5. Установить зависимости 
    ```bash
    pip install -r requirements.txt
    ```

6. Создать папку для сокета
    ```bash
    mkdir -r /run/uwsgi
    ```
7. Установить nginx 
    ```bash
    sudo apt-get update && sudo apt-get install nginx
    ```

8. Создать конфигурацию для проекта 

    Перейти:
    ```bash
    sudo nano /etc/nginx/sites-available/django_form_handler
    ```

    Вставить:
    ```bash
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

    `YOUR_SERVER_IP` - IP виртуальной машины (например 123.45.67.89), айпи можно узнать командой `ip addr show` (интерфейс inet)

9. Создать символическую ссылку

    ```bash
    sudo ln -s /etc/nginx/sites-available/django_form_handler/etc/nginx/sites-enabled/
    ```

10. Проверить конфигурацию
    ```
    sudo nginx -t
    ```

11. Перезапуск nginx
    ```bash
    sudo systemctl restart nginx
    ```

12. Добавить по пути `django_form_handler/settings.py` в `ALLOWED_HOSTS` наш айпи адрес сервера

13. Скачиваем PostgreSQL, включаем службу
    ```bash
    sudo apt install postgresql postgresql-contrib -y
    sudo systemctl start postgresql
    sudo systemctl enable postgresql
    sudo systemctl status postgresql 
    ```


14. Создаем БД и пользователя.
    Зайти в БД.
    ```bash
    sudo -u postgres psql
    ```
    ```sql
    CREATE USER root WITH PASSWORD '123321';
    CREATE DATABASE mydatabase OWNER root;
    GRANT ALL PRIVILEGES ON DATABASE mydatabase TO root;
    ```

    Проверить успешного создания
    ```bash
    \l
    ```

    Выход
    ```
    \q
    ```

15. Экспортировать переменные окружения
    ```
    export DB_USER="root"
    export DB_PASS="123321"
    export DB_NAME="mydatabase"
    export DB_HOST="localhost"
    export DB_PORT="5432"
    ```


16. Запустить проект

    ```bash
    cd /home/xdxd1488/django_form_handler/  
    ```

    ```bash
    uwsgi --ini uwsgi.ini --daemonize uwsgi.log
    ```

---

P.S.

Выключить проект  sudo pkill -f uwsgi


Сайт теперь доступен по ссылке `http://185.244.50.155:1488/` и `http://185.244.50.155:1488/list`
рабочая ссылка, собственный VPS, можно проверить работу
