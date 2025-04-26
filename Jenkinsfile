pipeline {
    agent any

    environment {
        DJANGO_SETTINGS_MODULE = "iot_backend.settings"  // (fix this too, it was wrong before)
    }

    stages {
        stage('Pull Code') {
            steps {
                echo 'Pulling latest code from GitHub...'
                sh 'git pull origin main'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                echo 'Creating virtual environment...'
                sh '''
                    cd iot_project
                    python3 -m venv venv
                    ./venv/bin/pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python packages...'
                sh '''
                    cd iot_project
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Django Migrations') {
            steps {
                echo 'Running Django migrations...'
                sh '''
                    cd iot_project
                    ./venv/bin/python manage.py migrate
                '''
            }
        }

        stage('Collect Static Files') {
            steps {
                echo 'Collecting static files...'
                sh '''
                    cd iot_project
                    ./venv/bin/python manage.py collectstatic --noinput
                '''
            }
        }

        stage('Restart Gunicorn') {
            steps {
                echo 'Restarting Gunicorn...'
                sh 'sudo systemctl restart gunicorn'
            }
        }
    }
}

