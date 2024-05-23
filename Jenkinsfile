pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "jenkins-cat:alpine"
        DOCKER_CONTAINER_NAME = "jenkins-cat"
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Eliminar la carpeta si ya existe
                    sh 'rm -rf JENKINS-APP-WEB'
                    // Clonar el repositorio manualmente
                    sh 'git clone https://github.com/HectorHYM/JENKINS-APP-WEB.git'
                    sh 'cd JENKINS-APP-WEB && git checkout main'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // Construir la imagen Docker
                    sh 'cd JENKINS-APP-WEB && docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    // Detener y eliminar el contenedor si ya existe
                    sh 'docker stop ${DOCKER_CONTAINER_NAME} || true'
                    sh 'docker rm ${DOCKER_CONTAINER_NAME} || true'

                    // Ejecutar el nuevo contenedor
                    sh 'docker run -d -p 5000:5000 --name ${DOCKER_CONTAINER_NAME} ${DOCKER_IMAGE}'
                }
            }
        }
    }

    post {
        success {
            echo 'La aplicación Flask se ha desplegado correctamente'
        }
        failure {
            echo 'La construcción o el despliegue han fallado'
        }
    }
}
