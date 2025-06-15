pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIAL_ID = 'dockerhub_credential' // Jenkins'de tanımlı DockerHub credential ID'si
        DOCKERHUB_USERNAME = 'elllliif'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${env.DOCKERHUB_USERNAME}/system-monitor:latest")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIAL_ID) {
                        docker.image("${env.DOCKERHUB_USERNAME}/system-monitor:latest").push()
                    }
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    docker rm -f jenkins-blueocean || true
                    docker run -d --name jenkins-blueocean ${DOCKERHUB_USERNAME}/system-monitor:latest
                '''
            }
        }
    }
}
