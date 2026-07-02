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
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Install Playwright browsers') {
            steps {
                sh '''
                    . venv/bin/activate
                    playwright install --with-deps
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --junitxml=result.xml
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'result.xml'
        }
    }
}
