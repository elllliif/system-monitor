pipeline {
    agent any

    environment {
        GIT_CREDENTIALS_ID = 'project_etabakli' // Jenkins Credential ID
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/elllliif/system-monitor.git',
                        credentialsId: "${env.GIT_CREDENTIALS_ID}"
                    ]]
                ])
            }
        }

        stage('Update code') {
            steps {
                // Örneğin bir dosya düzenleniyor, script çalıştırılıyor vs.
                sh 'echo "Yeni satır" >> README.md'
            }
        }

        stage('Commit and Push') {
            steps {
                // Git config ayarları (opsiyonel, ama genelde gerekli)
                sh '''
                    git config user.email "elif772017@icloud.com"
                    git config user.name "Elif"
                    git add .
                    git commit -m "Automated update from Jenkins"
                    git push origin main
                '''
            }
        }

        stage('Build and Run') {
            steps {
                sh 'docker build -t system-monitor .'
                sh 'docker run -d --name system-monitor-container system-monitor'
            }
        }
    }
}
