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
                bat 'docker run ev-app pytest'
            }
        }
        stage('Security Scan') {
    steps {
        bat 'docker run ev-app bandit -r . -ll -x tests/'
    }
}

        stage('Run Container') {
            steps {
                bat 'docker rm -f ev-container || exit 0'
                bat 'docker run -d -p 5000:5000 --name ev-container ev-app'
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