pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/suganthirosir-cell/newrepository.git'
            }
        }

        stage('Install') {
            steps {
                bat 'pip install streamlit'
            }
        }

        stage('Run App') {
            steps {
                bat 'streamlit run app.py --server.headless true'
            }
        }
    }
}
