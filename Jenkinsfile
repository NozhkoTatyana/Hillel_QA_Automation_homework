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

                    pip install --upgrade pip
                    pip install -r requirements.txt

                    playwright install chromium
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                     export PYTHONIOENCODING=utf-8
                     export LANG=C.UTF-8
                     export LC_ALL=C.UTF-8

                    pytest \
                        --ignore=lesson_13 \
                        --ignore=lesson_30 \
                        --ignore=lesson_29 \
                        --ignore=lesson_24 \
                        --junitxml=result.xml \
                        --alluredir=allure-results

                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true,
                  testResults: 'result.xml'
        }
    }
}