pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS = credentials('GITHUB_CREDENTIAL_ID')
    }

    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: 'MY_SECRET_KEY', url: 'https://github.com/NirukoX/c-cd-jenkins-demo.git', branch: 'main'
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
