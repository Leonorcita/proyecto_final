pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Leonorcita/proyecto_final.git'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
        
        stage('Linting') {
            steps {
                sh 'flake8 .'
            }
        }
        
        stage('Build Docker Image') {
            when {
                anyOf {
                    branch 'develop'
                    branch 'main'
                }
            }
            steps {
                script {
                    docker.build("imagendockerleonor:latest")
                }
            }
        }
        
        stage('Push Docker Image') {
            when {
                anyOf {
                    branch 'develop'
                    branch 'main'
                }
            }
            steps {
                script {
                    docker.withRegistry('https://hub.docker.com/', 'leonorcita') {
                        docker.image("imagendockerleonor:latest").push()
                    }
                }
            }
        }
    }
}
