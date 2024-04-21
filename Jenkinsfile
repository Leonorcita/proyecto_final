pipeline {
    agent any
    
    stages {
        stage('Check Python Installation') {
            steps {
                script {
                    // Verificar si Python está instalado
                    if (!isPythonInstalled()) {
                        // Instalar Python
                        sh 'sudo apt-get update'
                        sh 'sudo apt-get install -y python3'
                    }
                }
            }
        }
        
        stage('Create Virtual Environment') {
            steps {
                script {
                    // Crear el entorno virtual
                    sh 'python3 -m venv /var/jenkins_home/workspace/myenv'
                    // Activar el entorno virtual
                    sh 'source /var/jenkins_home/workspace/myenv/bin/activate'
                }
            }
        }
        
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Leonorcita/proyecto_final.git'
            }
        }
        
        stage('Install Requirements') {
            steps {
                script {
                    // Instalar las dependencias del proyecto en el entorno virtual
                    sh 'pip install -r proyecto_final/requirements.txt'
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                // Ejecutar pruebas usando make pytest
                sh 'make pytest'
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
                    // Construir la imagen Docker
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
                    // Utiliza las credenciales de Docker Hub
                    withCredentials([usernamePassword(credentialsId: 'DOCKHUB', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        // Loguearse en Docker Hub
                        sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                        
                        // Subir la imagen a Docker Hub
                        docker.withRegistry('https://hub.docker.com/', 'leonorcita') {
                            docker.image("imagendockerleonor:latest").push()
                        }
                    }
                }
            }
        }
    }
}

def isPythonInstalled() {
    // Verificar si Python está instalado
    return sh(script: 'command -v python3 &> /dev/null', returnStatus: true) == 0
}
