pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "jenkins-cat:latest"
        DOCKER_CONTAINER_NAME = "jenkins-cat"
    }

    stages {
        stage('Checkout') {
            steps {
                //Se clona el repositorio de Git
                git branch: 'main', url: 'https://github.com/HectorHYM/JENKINS-APP-WEB.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    //Se contruye la imagen Docker
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    //Se detiene y elimina el contenedor si ya existe
                    sh 'docker stop ${DOCKER_CONTAINER_NAME} || true'
                    sh 'dcoker rm ${DOCKER_CONTAINER_NAME} || true'

                    //Se ejecuta el nuevo contenedor
                    sh 'docker run -d -p 5000:5000 --name ${DOCKER_CONTAINER_NAME} ${DOCKER_IMAGE}'
                }
            }
        }
    }

    post {
        success {
            echo 'La aplicación Flask se ha desplegado correctamente'
        }
        failure{
            echo 'La construcción o el despliegue han fallado'
        }
    }
}