# Contributing To Market Analysis App

Thank you for considering contributing to the Market Analysis App project !

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setting up for Local Development](#setting-up-for-local-development)
3. [How to Report Bugs or Suggest Enhancements](#how-to-report-bugs-or-suggest-enhancements)
4. [Running Models Locally](#running-models-locally)
5. [Building and Tests](#building-and-tests)
6. [Commit Message Guidelines](#commit-message-guidelines)
7. [Pull Request Process](#pull-request-process)
8. [Coding Styleguides](#coding-styleguides)
9. [Continuous Integration/Continuous Deployment (CI/CD)](#continuous-integrationcontinuous-deployment-cicd)

### 1. Prerequisites

Before you begin contributing, please ensure that you meet the following prerequisites:

1. **Installation**: You should follow the installation steps.

### 2. Setting up for Local Development

**Note ->** Anytime you see text wrapped with these symbols - '<>' like '<chosen_virtual_environment_name>' it means that you are free to chose the name yourself.

1. **Setup Virtual Environment:**
    ```bash
    uv venv <chosen_virtual_environment_name> --python=3.14
    ```

2. **Activate Virtual Environment:**
    ```bash
    uv venv <chosen_virtual_environment_name>/bin/activate
    ```

3. **Install Requirements:**
    ```bash
    uv pip install -r requirements.txt
    ```
    **Note ->** Sometimes to recognise the new installations you will need to `deactivate` the virtual environment and then reactivate it.

    **ADR's ->** If you plan to PR a new ADR then you will need to install `adr-tools` you can find the installation steps [here](https://github.com/npryce/adr-tools/blob/master/INSTALL.md)

4. **Export Environment Variables:**
    ```bash
    export API_KEY="YOUR_API_KEY"
    ```