pipeline {
    agent any

    // Eğer webhook ile tetikliyorsan, triggers kısmını kaldırabilirsin.
    // triggers {
    //     pollSCM('H/5 * * * *')  // Alternatif: her 5 dakikada bir kontrol eder.
    // }
    
    environment {
        GIT_CREDENTIALS_ID = 'project_etabakli'
        DOCKERHUB_CREDENTIAL_ID = 'dockerhub_credential'
        DOCKERHUB_USERNAME = 'elllliif'
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
                sh 'echo "Yeni satır" >> README.md'
            }
        }

        stage('Commit and Push') {
            steps {
                script {
                    def changes = sh(script: 'git status --porcelain', returnStdout: true).trim()
                    if (changes) {
                        sh '''
                            git config user.email "elif772017@icloud.com"
                            git config user.name "Elif"
                            git add .
                            git commit -m "Automated update from Jenkins"
                            git push origin main
                        '''
                    } else {
                        echo "No changes to commit."
                    }
                }
            }
        }

        stage('Build, Push and Run') {
            steps {
                script {
                    // Docker Hub'a login ve push işlemi
                    docker.withRegistry('https://index.docker.io/v1/', "${env.DOCKERHUB_CREDENTIAL_ID}") {
                        sh """
                            docker build -t ${env.DOCKERHUB_USERNAME}/system-monitor:latest .
                            docker push ${env.DOCKERHUB_USERNAME}/system-monitor:latest
                        """
                    }
                    // Eğer önceki container varsa kaldır, yeni container çalıştır
                    sh '''
                        if [ $(docker ps -aq -f name=email_monitor) ]; then
                            docker rm -f email_monitor
                        fi
                        docker run -d --name email_monitor ${DOCKERHUB_USERNAME}/system-monitor:latest
                    '''
                }
            }
        }
    }
}
