pipeline {
    agent any

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', 
                          branches: [[name: 'main']], 
                          userRemoteConfigs: [[url: 'https://github.com/elllliif/system-monitor.git', credentialsId: 'project_etabakli']]])
            }
        }
        stage('Build and Run') {
            steps {
                sh 'docker build -t system-monitor .'
                sh 'docker stop system-monitor-container || true'
                sh 'docker rm system-monitor-container || true'
                sh 'docker run -d --name system-monitor-container system-monitor'
            }
        }
    }
}
