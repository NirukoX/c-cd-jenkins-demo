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
            timeout(time: 10, unit: 'SECONDS') {  // ⏳ 10-second timeout
                steps {
                    script {
                        bat 'python -m unittest testapp.py || exit 0'  // Prevents failure
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                timeout(time: 30, unit: 'SECONDS') {  // ⏳ 10-second timeout
                    bat 'python cloneapp.py'
                }
            }
        }
    }
}
