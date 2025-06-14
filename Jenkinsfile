pipeline {
    agent any

    triggers {
        githubPush()
    }
    
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
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub_credential') {
                        sh """
                            docker build -t elllliif/system_monitor:latest .
                            docker push elllliif/system_monitor:latest
                        """
                    }
                    sh '''
                        docker rm -f system_monitor-container || true
                        docker run -d --name system_monitor-container elllliif/system-monitor:latest
                    '''
                }
            }
        }

    }
}
