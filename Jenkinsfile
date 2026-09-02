pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Sahilx987/jenkins-demo-app.git'
            }
        }
        stage('Setup & Install') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
                sh './venv/bin/pip install pytest'
            }
        }
        stage('Test') {
            steps {
                sh './venv/bin/pytest test_main.py -v'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jenkins-demo-app:latest .'
            }
        }
    }
}
