pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockerhub-credential'   // Jenkins Credentials olarak Docker Hub kullanıcı adı + token buraya eklenmeli
        GIT_REPO = 'https://github.com/elllliif/system-monitor.git'
        GIT_BRANCH = 'main'                                // İstersen başka branch belirtebilirsin
        IMAGE_NAME = 'elllliif/system-monitor'             // Docker Hub repo ismi
        IMAGE_TAG = 'latest'
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
                    env.IMAGE_TAG = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                }
                echo "Building Docker image: ${IMAGE_NAME}:${env.IMAGE_TAG}"
                sh "docker build -t ${IMAGE_NAME}:${env.IMAGE_TAG} ."
            }
        }
        
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', "${DOCKERHUB_CREDENTIALS}") {
                        def dockerImage = docker.image("${IMAGE_NAME}:${IMAGE_TAG}")
                        echo "Pushing Docker image: ${IMAGE_NAME}:${IMAGE_TAG}"
                        dockerImage.push()
                    }
                }
            }
        }






        
    }
}
