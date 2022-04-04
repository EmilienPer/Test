pipeline {
    agent any

    stages {
        stage('SCM') {
            steps {
                git branch: 'develop', url: 'https://github.com/oxydedefer/DevopsTalk.git'
            }
        }
        stage('Build toolbox') {
            steps {
               sh 'docker build -f Dockerfile.python.toolbox -t talk-devops-toolbox:latest .'
            }
        }
        stage('Build Flask CI images') {
            steps {
               sh 'docker build --no-cache -f Dockerfile.python.ci -t talk-devops-app-build:latest .'
            }
        }
        stage('Testing') {
             parallel {
                stage('unit-test') {
                    steps {
                       sh 'docker run --rm -i talk-devops-app-build:latest python sample-test.py'
                    }
                }
                stage('Code analysis Sonarqube') {
                    steps {
                       sh """ docker run --rm -i talk-devops-app-build:latest sonar-scanner \
                                -Dsonar.projectKey=devops-talk \
                                -Dsonar.sources=. \
                                -Dsonar.host.url=http://host.docker.internal:9000 \
                                -Dsonar.qualitygate.wait=true\
                                -Dsonar.login=9a45255286579268e6beb7c11d04390f8fd79389"""
                    }
                }
             }
        }

        stage('build release image'){
            steps {
               sh 'docker build --no-cache -f Dockerfile.flask -t talk-devops-app:${GIT_COMMIT} .'
            }
        }

        stage('Deploy release images') {
            steps {
               
               withCredentials([string(credentialsId: 'HEROKU_API_KEY', variable: 'HEROKU_API_KEY_SECRET')]) {      
                    sh 'docker tag talk-devops-app:${GIT_COMMIT} registry.heroku.com/devops-talk/web'
                    sh 'HEROKU_API_KEY=${HEROKU_API_KEY_SECRET} heroku container:login'
                    sh 'docker push registry.heroku.com/devops-talk/web'
                    sh 'HEROKU_API_KEY=${HEROKU_API_KEY_SECRET} heroku container:release web --app devops-talk'
                    sh 'docker image rm registry.heroku.com/devops-talk/web'
                    
                } 
            }
        }
        stage('Clean Unused Docker image') {
            steps {
               sh 'docker image rm --force talk-devops-app-build:latest'
               sh 'docker image rm --force talk-devops-app:${GIT_COMMIT}'
            }
        }
    }
}
