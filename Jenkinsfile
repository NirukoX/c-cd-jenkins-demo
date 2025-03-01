pipeline {
    agent any

    environment {
        GITHUB_TOKEN = credentials('GITHUB_PAT')
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    bat '''
                    if exist c-cd-jenkins-demo (
                        rmdir /s /q c-cd-jenkins-demo
                    )
                    git clone https://%GITHUB_TOKEN%@github.com/NirukoX/c-cd-jenkins-demo.git
                    '''
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
                bat 'python -m unittest discover -s tests -p "testapp.py"'
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
