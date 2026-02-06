pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/suganthirosir-cell/newrepository.git'
            }
        }

        stage('Install') {
            steps {
                sh 'pip install streamlit'
            }
        }

        stage('Run App') {
            steps {
                sh 'streamlit run newapp.py --server.headless true --server.port 8501'
            }
        }
    }
}
