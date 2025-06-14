pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/kullanici/your-python-project.git'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python3 send_email.py'
            }
        }
    }
}
