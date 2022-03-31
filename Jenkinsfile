pipeline {
    agent any

    stages {
        stage('VCS') {
            steps {
                git branch: 'develop', url: 'https://github.com/oxydedefer/DevopsTalk.git'
            }
        }
        
        stage('Build') {
            steps {
               sh 'docker build -f Dockerfile.flask -t talk-devops-app:latest .'
            }
        }
        stage('Testing') {
             parallel {
                stage('unit-test') {
                    steps {
                       sh 'docker run -i talk-devops-app:latest python sample-test.py'
                    }
                }
             }
        }
    }
    
}