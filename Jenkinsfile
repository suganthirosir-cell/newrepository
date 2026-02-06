pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/suganthirosir-cell/newrepository.git'
            }
        }

        stage('Install') {
            steps {
                // Linux container → use sh
                sh 'pip install streamlit'
            }
        }

        stage('Run App') {
            steps {
                // Make sure file name matches your repo
                sh 'streamlit run newapp.py --server.headless true --server.port 8501'
            }
        }
    }
}
