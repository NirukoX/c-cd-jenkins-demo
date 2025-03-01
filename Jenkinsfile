pipeline {
    agent any

    environment {
        GITHUB_TOKEN = credentials('GITHUB_PAT')  // Securely fetch token from Jenkins
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    sh 'git clone https://$GITHUB_TOKEN@github.com/NirukoX/c-cd-jenkins-demo.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python -m unittest discover'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh 'python cloneapp.py &'
            }
        }
    }
}
