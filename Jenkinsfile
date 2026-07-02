pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Install Playwright browsers') {
            steps {
                sh 'playwright install'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest --junitxml=result.xml'
            }
        }
    }

    post {
        always {
            junit 'result.xml'
        }
    }
}