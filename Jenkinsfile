pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'python setup.py build'
      }
    }
    stage('clean') {
      steps {
        sh 'python setup.py clean --all'
      }
    }
  }
}