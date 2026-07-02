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
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'python3 -m pytest --junitxml=result.xml'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'result.xml'
        }
    }
}