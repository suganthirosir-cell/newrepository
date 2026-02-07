pipeline {
    agent any

    environment {
        APP_PORT = "8501"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/suganthirosir-cell/newreppipeline {
    agent any

    environment {
        APP_PORT = "8501"
    }

    stages {
        stage('Clone Repo') {s
            steps {
                git branch: 'main', url: 'https://github.com/suganthirosir-cell/newrepository.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Node.js http-server globally
                sh 'npm install -g http-server'
            }
        }

        stage('Run App') {
            steps {
                // Serve the HTML file on port 8501
                sh "http-server -p ${APP_PORT} -c-1"
            }
        }
    }
}
ository.git'
            }
        }

        stage('Run Streamlit in Docker') {
            steps {
                // Run Streamlit inside Python Docker container
                sh """
                docker run --rm -p ${APP_PORT}:${APP_PORT} -v \$WORKSPACE:/app -w /app python:3.11 bash -c \\
                "pip install -r requirements.txt && streamlit run newapp.py --server.headless true --server.port ${APP_PORT}"
                """
            }
        }
    }
}
