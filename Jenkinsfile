pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/elllliif/system-monitor.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t system-monitor .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                   docker stop system-monitor || true
                   docker rm system-monitor || true
                   docker run -d --name system-monitor system-monitor
                '''
            }
        }
    }
}
