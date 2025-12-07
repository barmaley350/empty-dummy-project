#!/bin/bash

# colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

PATH_TO_BACKEND="/services/backend"
PATH_TO_BACKEND_DOCS="/services/backend/docs"

# Абсолютный путь к каталогу скрипта
SCRIPT_DIR=$(cd -P "$(dirname -- "$0")" && pwd -P)

# Извлекаем только имя папки из полного пути
FOLDER_NAME=$(basename "$SCRIPT_DIR")

# text success
print_text_green() { 
    echo -en "${GREEN} \u2714 $1${NC}" 
}
# text error
print_text_red() {
    echo -en "${RED} \u2718 $1${NC}"
}
# text yellow
print_text_yellow() {
    echo -en "${YELLOW}$1${NC}"
}
# text blue
print_text_blue() {
    echo -en "${BLUE}$1${NC}"
}
# text white
print_text_white() {
    echo -en "$1"
}
print_text_block() {
    case $1 in
        success)
            line
            print_text_green "$2 \n" 
            line
            ;;
        error)
            line
            print_text_red "$2 \n"
            line
            ;;
    esac
}
# lines
line() {
    cols=$(tput cols)
    for ((i=1; i<=cols; i++)); do echo -en "\u2500"; done
    echo -e ""
}
line2() {
    cols=$(tput cols)
    for ((i=1; i<=cols; i++)); do echo -en "\u2500"; done
    echo -e ""
}

# help 
help() {
    
    line
    print_text_yellow "Справка по доступным командам\n"
    print_text_white "./run.sh [command] [command params]\n"
    print_text_white "[command] - Основная команда либо команда быстрого доступа\n"
    print_text_white "[command params] - Любые параметы которые принимает эта комманда\n"
    line2    
    print_text_white "[command] - основные команды\n"
    print_text_blue "help | empty"
    print_text_white " \u2501 Вывод справки\n"
    print_text_blue "manage [params]"
    print_text_white " \u2501 Запуск manage.py в backend контейнере\n"    
    print_text_blue "pytest [params]"
    print_text_white " \u2501 Запуск pytest в backend контейнере \n"    
    print_text_blue "shell"
    print_text_white " \u2501 Запуск /bin/bash в backend контейнере для ручного выполнения команд\n" 
    line2 
    print_text_white "[command] - Команды быстрого доступа\n"
    print_text_blue "gendoc"
    print_text_white " \u2501 Генерация Sphinx документации\n" 
    print_text_blue "ruffcheck"
    print_text_white " \u2501 Запуск ruff check\n"     
    print_text_blue "ruffformat"
    print_text_white " \u2501 Запуск ruff format\n"   
    print_text_blue "ruff"
    print_text_white " \u2501 Запуск ruff check и ruff format\n"       
    print_text_blue "commit"
    print_text_white " \u2501 Запуск gendoc, ruff check, ruff format и pytest\n"      

    echo -e ""
}
# pytest
command_pytest() {
    docker exec -it ${FOLDER_NAME}-service.backend-1 pipenv run pytest "$@"
}
# manage
command_manage() {
    docker exec -it ${FOLDER_NAME}-service.backend-1 pipenv run python3 manage.py "$@"
}
# docker shell
command_shell() {
    docker exec -it ${FOLDER_NAME}-service.backend-1 /bin/bash
}
# docker shell
command_shell() {
    docker exec -it ${FOLDER_NAME}-service.backend-1 /bin/bash
}
# gendoc
command_gendoc() {
    generate_graph_models
    generate_sphinx_docs
} 
generate_sphinx_docs() {
    cd $SCRIPT_DIR$PATH_TO_BACKEND_DOCS
    pipenv run make clean
    pipenv run make html

    if [ $? -ne 0 ]; then
        print_text_block error "Ошибка при создании документации Sphinx"  
        exit $?
    fi

    print_text_block success "Генерация документации Sphinx прошла успешно"
    return 0
}


# Generate sphinx docs for backend/django
generate_graph_models() {
    cd $SCRIPT_DIR$PATH_TO_BACKEND
    print_text_white "Создаем graph_models testapp -o docs/_static/testapp.png\n"
    pipenv run python3 manage.py graph_models testapp -o docs/_static/testapp.png

    print_text_white "Создаем graph_models sphinx_docs -o docs/_static/sphinx_docs.png\n"
    pipenv run python3 manage.py graph_models sphinx_docs -o docs/_static/sphinx_docs.png

    print_text_white "Создаем graph_models -o docs/_static/all.png\n"
    pipenv run python3 manage.py graph_models -o docs/_static/all.png

    if [ $? -ne 0 ]; then
        print_text_block error "Генерация graph_models структуры DB завершилась с ошибкой"
        exit $?
    fi
    cp docs/_static/* $SCRIPT_DIR/files/img/graph_models

    print_text_block success "Генерация graph_models структуры DB прошла успешно"
    return 0
}

command_ruff_check() {
    cd $SCRIPT_DIR$PATH_TO_BACKEND

    pipenv run ruff check "$@"

    if [ $? -ne 0 ]; then
        print_text_block error "Есть ошибки при выполнении ruff check $@"
        exit $?
    fi
    print_text_block success "Успешное завершение ruff check $@"
    return 0
}

command_ruff_format() {
    # Ruff formater backend/django
    cd $SCRIPT_DIR$PATH_TO_BACKEND
    pipenv run ruff format

    if [ $? -ne 0 ]; then
        print_text_block error "сть ошибки при выполнении ruff format $@"
        exit $?
    fi
    print_text_block success "Успешное завершение ruff format $@"
}
command_ruff() {
    command_ruff_check
    command_ruff_format
}
# commit
command_commit() {
    command_gendoc
    command_ruff
    command_pytest
}
# main
main() {
    if [ $# -eq 0 ]; then
        help
        exit 0
    fi

    command=$1
    shift

    case $command in
        help)
            help "$@"
            ;;    
        shell)
            command_shell "$@"
            ;;
        manage)
            command_manage "$@"
            ;;  
        pytest)
            command_pytest "$@"
            ;;     
        gendoc)
            command_gendoc "$@"
            ;;    
        ruffcheck)
            command_ruff_check "$@"
            ;;   
        ruffformat)
            command_ruff_format "$@"
            ;;   
        ruff)
            command_ruff
            ;;      
        commit)
            command_commit
            ;;                                                       
        *)
            print_text_error "Не известная комманда - $command"
            ;;        
    esac    
}

main "$@" 