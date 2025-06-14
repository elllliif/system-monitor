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
                sh 'docker run --rm system-monitor'
            }
        }
    }
}
