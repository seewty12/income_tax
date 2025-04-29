pipeline{
    agent any

    stages{
        stage("checkout code"){
            steps{
                git credentialsId:"demo_project1 ",url:"https://github.com/seewty12/income_tax.git" , branch:"main"
          }

        }
        stage("install dependencies"){
            steps{
                bat '''
                python -m venv venv
                call venv \\scripts\\activate
                pip install --upgrade pip
                '''
            }
        }
        stage("run python scripts"){
            steps{
                bat '''
                call venv\\scripts\\avtivate
                python sign_up.py
                '''
            }
        }
        stage("deploy application"){
            steps{
                echo "deploying application"
            }
        }
    }
    post{
        success{
            echo "pipeline successfully"
        }
        failure{
            echo "pipeline failutre"
        }
    }
}