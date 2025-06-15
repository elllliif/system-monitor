pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-credentials'   // Jenkins Credentials olarak Docker Hub kullanıcı adı + token buraya eklenmeli
        GIT_REPO = 'https://github.com/elllliif/system-monitor.git'
        GIT_BRANCH = 'main'                                // İstersen başka branch belirtebilirsin
        IMAGE_NAME = 'elllliif/system-monitor'             // Docker Hub repo ismi
        IMAGE_TAG = ''
    }

    stages {
        stage('Checkout') {
            steps {
                git url: "${GIT_REPO}", branch: "${GIT_BRANCH}"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    IMAGE_TAG = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                }
                echo "Building Docker image: ${IMAGE_NAME}:${IMAGE_TAG}"
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Login DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', "${DOCKERHUB_CREDENTIALS}") {
                        echo 'Logged in to Docker Hub'
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', "${DOCKERHUB_CREDENTIALS}") {
                        sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                    }
                }
            }
        }
    }
}
