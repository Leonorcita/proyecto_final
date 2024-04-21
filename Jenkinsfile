pipeline {
    agent any
    
    stages {
        stage('Check Python and Make Installation') {
            steps {
                script {
                    // Verificar si Python está instalado
                    if (!isPythonInstalled()) {

                        sh 'echo "Python no está instalado. Contacte con el equipo de infraestructura.'
                    }

                    // Verificar si Make está instalado
                    if (!isMakeInstalled()) {

                        sh 'echo "Make no está instalado. Contacte con el equipo de infraestructura.'
                    }
                }
            }
        }
      
        stage('Clone Repository') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/develop']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'GITHUB', url: 'https://github.com/Leonorcita/proyecto_final.git']]])
            }
        }
        
        stage('Install Requirements') {
            steps {
                script {
                        // Crear el entorno virtual
                        sh 'python3 -m venv myenv'

                        // Activar el entorno virtual
                        sh 'source myenv/bin/activate'

                        // Instalar las dependencias del proyecto
                        sh 'source myenv/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                // Ejecutar pruebas usando make pytest
                sh 'source myenv/bin/activate && make pytest'
            }
        }
        
        stage('Linting') {
            steps {
                sh 'source myenv/bin/activate && flake8 .'
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

def isMakeInstalled() {
    // Verificar si Make está instalado
    return sh(script: 'command -v make &> /dev/null', returnStatus: true) == 0
}
