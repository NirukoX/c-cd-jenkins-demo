pipeline {
    agent any

    environment {
        GITHUB_TOKEN = credentials('GITHUB_PAT')
    }

    stages {
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
