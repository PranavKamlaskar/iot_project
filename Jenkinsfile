pipeline {
    agent any

    environment {
        PROJECT_DIR = "/home/ubuntu/iot_project"
        VENV_DIR = "/home/ubuntu/iot_project/venv"
        GUNICORN_SOCKET = "/home/ubuntu/iot_project/iot_backend.sock"
    }

    stages {
        stage('Pull Code') {
            steps {
                echo 'Pulling latest code from GitHub...'
                sh 'git pull origin main'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python packages...'
                sh '${VENV_DIR}/bin/pip install -r ${PROJECT_DIR}/requirements.txt'
            }
        }

        stage('Run Django Migrations') {
            steps {
                echo 'Applying Django migrations...'
                sh '${VENV_DIR}/bin/python ${PROJECT_DIR}/manage.py migrate'
            }
        }

        stage('Collect Static Files') {
            steps {
                echo 'Collecting static files...'
                sh 'echo yes | ${VENV_DIR}/bin/python ${PROJECT_DIR}/manage.py collectstatic'
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

