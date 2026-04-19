pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t ev-app .'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest'
            }
        }

        stage('Security Scan') {
            steps {
                bat 'pip install bandit'
                bat 'bandit -r .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 ev-app'
            }
        }

        stage('Release') {
            steps {
                echo 'Application released v1.0'
            }
        }

        stage('Monitoring') {
            steps {
                echo 'Application running and logs monitored'
            }
        }
    }
}