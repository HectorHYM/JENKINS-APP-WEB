pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "jenkins-cat:alpine"
        DOCKER_CONTAINER_NAME = "jenkins-cat"
        SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/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'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    try {
                        // Eliminar la carpeta si ya existe
                        sh 'rm -rf JENKINS-APP-WEB'
                        // Clonar el repositorio manualmente
                        sh 'git clone https://github.com/HectorHYM/JENKINS-APP-WEB.git'
                        sh 'cd JENKINS-APP-WEB && git checkout main'
                        // Notificación de éxito a Slack
                        sh """
                        curl -X POST -H 'Content-type: application/json' --data '{"text":"Checkout stage completed successfully: ${env.JOB_NAME} #${env.BUILD_NUMBER}"}' ${SLACK_WEBHOOK_URL}
                        """
                    } catch (Exception e) {
                        // Notificación de fallo a Slack
                        sh """
                        curl -X POST -H 'Content-type: application/json' --data '{"text":"Checkout stage failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}"}' ${SLACK_WEBHOOK_URL}
                        """
                        throw e
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    try {
                        // Construir la imagen Docker
                        sh 'cd JENKINS-APP-WEB && docker build -t ${DOCKER_IMAGE} .'
                        // Notificación de éxito a Slack
                        sh """
                        curl -X POST -H 'Content-type: application/json' --data '{"text":"Build Docker Image stage completed successfully: ${env.JOB_NAME} #${env.BUILD_NUMBER}"}' ${SLACK_WEBHOOK_URL}
                        """
                    } catch (Exception e) {
                        // Notificación de fallo a Slack
                        sh """
                        curl -X POST -H 'Content-type: application/json' --data '{"text":"Build Docker Image stage failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}"}' ${SLACK_WEBHOOK_URL}
                        """
                        throw e
                    }
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    try {
                        // Detener y eliminar el contenedor si ya existe
                        sh 'docker stop ${DOCKER_CONTAINER_NAME} || true'
                        sh 'docker rm ${DOCKER_CONTAINER_NAME} || true'

                        // Ejecutar el nuevo contenedor
                        sh 'docker run -d -p 5000:5000 --name ${DOCKER_CONTAINER_NAME} ${DOCKER_IMAGE}'
                        // Notificación de éxito a Slack
                        sh """
                        curl -X POST -H 'Content-type: application/json' --data '{"text":"Run Docker Container stage completed successfully: ${env.JOB_NAME} #${env.BUILD_NUMBER}"}' ${SLACK_WEBHOOK_URL}
                        """
                    } catch (Exception e) {
                        // Notificación de fallo a Slack
                        sh """
                        curl -X POST -H 'Content-type: application/json' --data '{"text":"Run Docker Container stage failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}"}' ${SLACK_WEBHOOK_URL}
                        """
                        throw e
                    }
                }
            }
        }
    }

    post {
        success {
            script {
                // Notificación de éxito a Slack
                sh """
                curl -X POST -H 'Content-type: application/json' --data '{"text":"Pipeline executed successfully: ${env.JOB_NAME} #${env.BUILD_NUMBER}\\n${env.BUILD_URL}"}' ${SLACK_WEBHOOK_URL}
                """
            }
            echo 'La aplicación Flask se ha desplegado correctamente'
        }
        failure {
            script {
                // Notificación de fallo a Slack
                sh """
                curl -X POST -H 'Content-type: application/json' --data '{"text":"Pipeline execution failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}\\n${env.BUILD_URL}"}' ${SLACK_WEBHOOK_URL}
                """
            }
            echo 'La construcción o el despliegue han fallado'
        }
        always {
            script {
                // Obtener las últimas 10 líneas del log de la consola actual
                def summaryLog = ""
                try {
                    summaryLog = currentBuild.rawBuild.getLog(10).join('\n')
                } catch (Exception e) {
                    summaryLog = "No summary log available."
                }
                sh """
                curl -X POST -H 'Content-type: application/json' --data '{"text":"Build Log Summary for ${env.JOB_NAME} #${env.BUILD_NUMBER}:\\n${summaryLog}"}' ${SLACK_WEBHOOK_URL}
                """
            }
        }
    }
}
