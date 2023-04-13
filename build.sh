 set -o errexit
 pip install -r requirements.txt
 python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --upload-unhashed-files --no-input