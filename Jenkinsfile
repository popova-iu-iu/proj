pipeline {
    agent any

    environment {
        // Настройки для Allure
        ALLURE_RESULTS = "allure-results"
        ALLURE_REPORT = "allure-report"
    }

    stages {
        stage('Подготовка') {
            steps {
                echo "Установка зависимостей..."
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Запуск тестов') {
            steps {
                echo "Запуск тестов..."
                bat 'pytest --alluredir=${ALLURE_RESULTS} --reruns 2'  // Запуск тестов с повтором упавших
            }
        }

        stage('Генерация отчета Allure') {
            steps {
                echo "Генерация отчета Allure..."
                bat 'allure generate ${ALLURE_RESULTS} -o ${ALLURE_REPORT} --clean'
            }
        }

        stage('Сохранение артефактов') {
            steps {
                echo "Сохранение артефактов..."
                archiveArtifacts artifacts: '${ALLURE_REPORT}/**', onlyIfSuccessful: true
            }
        }
    }

    post {
        always {
            echo "Очистка и завершение..."
            allure includeProperties: false, jdk: '', results: [[path: "${ALLURE_RESULTS}"]]
        }
        failure {
            echo "Тесты упали! Отправка уведомления в Slack..."

        }
        success {
            echo "Тесты прошли успешно!"

        }
    }
}