pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'calculator-2'
        GITHUB_REPO_URL = 'https://github.com/nitish757/SPE-Calculator.git'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main', url: "${GITHUB_REPO_URL}"
                }
            }
        }

        stage('Build and Test') {
            steps {
                script {
                    sh 'python3 -m unittest test.py'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE_NAME}", '.')
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    docker.withRegistry('', 'DockerHubCred') {
                        sh 'docker tag calculator-2 nitish757/calculator:latest'
                        sh 'docker push nitish757/calculator-2'
                    }
                }
            }
        }

        stage('Run Ansible Playbook') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'inventory'
                    )
                }
            }
        }
    }
}