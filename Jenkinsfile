pipeline {
    agent any

    environment {
        APP_PORT = "8501"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/suganthirosir-cell/newrepository.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm install -g http-server'
            }
        }

        stage('Run App') {
            steps {
                sh "http-server -p ${APP_PORT} -c-1"
            }
        }
    }
}
