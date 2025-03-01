pipeline {
    agent any

    environment {
        GITHUB_TOKEN = credentials('GITHUB_PAT')
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    bat 'git clone https://%GITHUB_TOKEN%@github.com/NirukoX/c-cd-jenkins-demo.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install flask'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'python -m unittest discover'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                bat 'python cloneapp.py'
            }
        }
    }
}
