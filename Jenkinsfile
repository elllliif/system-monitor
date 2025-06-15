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
                    env.IMAGE_TAG = sh(script: "git rev-parse --short HEAD", returnStdout: true).trim()
                }
                echo "Building Docker image: ${IMAGE_NAME}:${env.IMAGE_TAG}"
                sh "docker build -t ${IMAGE_NAME}:${env.IMAGE_TAG} ."
            }
        }

    
       stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CREDENTIALS}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh """
                        echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin
                    """
                }
            }
        }


        stage('Push Docker Image') {
            steps {
                echo "Pushing Docker image: ${IMAGE_NAME}:${env.IMAGE_TAG}"
                sh "docker push ${IMAGE_NAME}:${env.IMAGE_TAG}"
            }
        }

        
    }
}
