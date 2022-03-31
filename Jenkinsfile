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
               sh 'docker build -f Dockerfile.python.ci -t talk-devops-app:latest .'
            }
        }
        stage('Testing') {
             parallel {
                stage('unit-test') {
                    steps {
                       sh 'docker run -i talk-devops-app:latest python sample-test.py'
                    }
                }
                stage('Code analysis Sonarqube') {
                    steps {
                       sh """ docker run --rm -i testsonar:latest /sonar-scanner/bin/sonar-scanner \
                                -Dsonar.projectKey=devops-talk \
                                -Dsonar.sources=. \
                                -Dsonar.host.url=http://192.168.1.142:9000 \
                                -Dsonar.login=145320bcea88d369d3e027c16417fee59895bfdd"""
                    }
                }
             }
        }
    }
    
}